import yaml
import subprocess
import json
import regex as re


def ReadFormDirs(dir):
    cmd = 'ls {}'.format(dir)
    files = subprocess.check_output(cmd, shell=True)
    myhosts = {}
    for file in files.split():
        with open('{}/{}'.format(dir, file),'r') as f:
            myhosts[file] = json.load(f)

    return myhosts


def get_host_by_seri(data):
         return data["HostName"]



def get_seri(host):
    return host['ansible_facts']['ansible_product_serial']



if __name__ == "__main__":

    with open("server_detail.yml", 'r') as f:
        datas = yaml.safe_load(f)

    host_data = []
    for i in datas:
        host_data.append(get_host_by_seri(datas[i]))

    csv_file = 'file/test123.csv'
    csv_osoa_file = 'file/124.csv'
    hosts_dir = ["live-out", "hub_out", "output"]
    my_hosts = {}
    for i in hosts_dir:
        my_hosts.update(ReadFormDirs(i))

    print len(host_data)
    print len(my_hosts)

    for i in my_hosts:
        seri = get_seri(my_hosts[i])
        if seri not in datas:
            print i, seri

