#!/usr/bin/env python3

import subprocess
import threading

def ping_hosts(cmd, close_fds=True, shell=True):
    child = subprocess.Popen(cmd)
    status,_ = child.communicate()
    return status

if __name__ == "__main__":
    threads = []
    ip_list = ['192.168.1.2', '192.168.1.3']
    for i in ip_list:
        if len(threads) <= 10:
            threading.Thread(name='ping {}'.format(i), target=ping_hosts(['/bin/ping', '-c 3', '{}'.format(i)]))
        else:
            pass