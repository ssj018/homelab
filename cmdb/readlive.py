#-*-coding:utf-8-*-
import json
import subprocess
import readcsv
import regex as re
import yaml
import sys


class ReadLiveInfo:
    def __init__(self, dirs):
        self.dirs = dirs
        self.my_hosts = {}
        if isinstance(self.dirs, list):
            for i in dirs:
                self.my_hosts.update(self.ReadFormDirs(i))
        else:
            self.my_hosts.update(self.ReadFormDirs(dirs))

    def ReadFormDirs(self, mydir):
        cmd = 'ls {}'.format(mydir)
        files = subprocess.check_output(cmd, shell=True)
        myhosts = {}
        for file in files.split():
            with open('{}/{}'.format(mydir, file), 'r') as f:
                myhosts[file] = json.load(f)
        return myhosts


    def get_nic_ip_mac(self,host):
        interfaces = self.my_hosts[host]['ansible_facts'].get('ansible_interfaces')
        devices = {}
        ips = {}
        macs = {}
        nics_info = {}
        for i in interfaces:
            device = "ansible_" + i
            devices[i] = self.my_hosts[host]['ansible_facts'].get(device, {})
            if 'macaddress' in devices[i] and devices[i]['active'] == True:
                macs[i] = devices[i]['macaddress']

            if i != "lo" and 'ipv4' in devices[i] and devices[i]['active'] == True:
                ips[i] = devices[i]["ipv4"]["address"]

        set1 = set(macs.keys())
        set2 = set(ips.keys())
        sets = set1.intersection(set2)
        for i in sets:
            nics_info[i] ='{}/{}'.format(ips[i], macs[i])
        return nics_info

    def get_seri(self,host):
        return self.my_hosts[host]['ansible_facts']['ansible_product_serial']

    def get_productName(self,host):
        return self.my_hosts[host]["ansible_facts"]["ansible_product_name"]


if __name__ == "__main__":
    hosts_dir = ["live-out", "hub_out", "output"]
    liveinfo = ReadLiveInfo(hosts_dir)
    print liveinfo.get_seri('ciytradea1')
    print liveinfo.get_productName('furion1')
    print liveinfo.get_nic_ip_mac("zeus5")

