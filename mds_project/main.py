import copy
import hashlib
import os
import time
from argparse import ArgumentParser
from multiprocessing import Pool, Process, Queue

import yaml


def do_remote_cmd(_server, _test):
    # scp files needed to remote
    assert os.system("ssh {} mkdir -p bin".format(_server["host"])) == 0
    assert os.system("ssh {} mkdir -p conf".format(_server["host"])) == 0
    assert os.system("ssh {} mkdir -p output".format(_server["host"])) == 0
    for i in _test["input"]:
        assert os.system("scp {} {}:{}".format(i, _server["host"], i)) == 0
    # run remote cmd
    assert os.system("ssh {} {}".format(_server["host"], _test["exec"])) == 0
    # scp remote output files to local if necessary
    if _test.get("output") and _test.get("output_hash"):
        tmp_output = "/tmp/{}/{}".format(_server["host"], _test["name"])
        os.makedirs(tmp_output, exist_ok=True)
        assert (
            os.system(
                "scp {}:{} {}".format(_server["host"], _test["output"], tmp_output)
            )
            == 0
        )
        # sum all output files up
        tmp = b""
        for filename in os.listdir(tmp_output):
            with open(os.path.join(tmp_output, filename), "rb") as f:
                tmp += f.read()
        assert hashlib.md5(tmp).hexdigest() == _test["output_hash"]


def do_test(_server, _test, _queue):
    for _ in range(_test.get("reties", 1)):
        with Pool(1) as p:
            try:
                ret = p.apply_async(do_remote_cmd, (_server, _test))
                ret.get(_test.get("timeout"))
                print("[{}] at [{}] succeed.".format(_test["name"], _server["host"]))
                _queue.put(1)
                break
            except Exception as e:
                p.terminate()
    else:
        print("[{}] at [{}] failed.".format(_test["name"], _server["host"]))
        _queue.put(0)


def create_pool(_server, _tests, _queue):
    # create a pool for each server to manage each test
    wait_buf = [
        Process(target=do_test, args=(_server, test, _queue)) for test in _tests
    ]
    wait_buf.reverse()
    run_buf = []
    while wait_buf or run_buf:
        # pop closed process
        for i, p in enumerate(run_buf):
            if not p.is_alive():
                run_buf.pop(i)
        # add test to pool if available
        while len(run_buf) < _server["capacity"] and wait_buf:
            p = wait_buf.pop()
            p.start()
            run_buf.append(p)
        # wait for some time
        time.sleep(0.1)


def replace_str(_str: str, _vars: dict):
    for k, v in _vars.items():
        _str = _str.replace("{{{{ {} }}}}".format(k), v)
    return _str


def main(_config: dict):
    global_variables: dict = _config["global_variables"]

    # replace vars in input or exec
    for test in _config["tests"]:
        # update local vars to global vars
        variables: dict = copy.copy(global_variables)
        variables.update(test.get("local_variables", {}))
        # replace vars in input and exec
        for i in range(len(test["input"])):
            test["input"][i] = replace_str(test["input"][i], variables)
        test["exec"] = replace_str(test["exec"], variables)

    # use a pool to manage all server
    queue = Queue()
    p_list = [
        Process(target=create_pool, args=(server, _config["tests"], queue))
        for server in _config["servers"]
    ]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

    # count all returns
    succeed = 0
    failed = 0
    for _ in _config["servers"]:
        for _ in _config["tests"]:
            if queue.get_nowait():
                succeed += 1
            else:
                failed += 1
    print("{} succeed. {} failed".format(succeed, failed))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--config", help="path to config yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.load(f)
    main(config)
