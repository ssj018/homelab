#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import codecs
import json
import readlive
import regex as re


def get_cur_location(host):
    if re.match('^gds',host):
        cur_location ='外高桥万国数据中心（华京路6号）'
    elif re.match('^cdg', host):
        cur_location = '大连高新机房'
    elif re.match('^cij',host):
        cur_location = '张江机房（乐昌路399号）'
    elif re.match('^hai.*(?<!mon|mon\d)$',host):
        cur_location = "数讯机房（秦桥路368号）"
    elif re.match('^wks',host):
        cur_location = "五矿"
    elif re.match('^cwg',host):
        cur_location = "中信证券上证通（华京路１号）"
    elif re.match('^csz',host):
        cur_location = '中信证券深证南方机房'
    elif re.match('^ciy',host):
        ciy1host = ['ciytradea3','ciytradea4','ciytrip1','ciyquote1','ciydatalog']
        if host in ciy1host:
            cur_location = "中信期货移动机房一期（宁桥路600号）"
        else:
            cur_location = "中信期货移动机房二期（宁桥路500号）"
    elif re.match("zeus5|mdstrademon[34]|pfsense-hubdc",host):
        cur_location = "hub dc (秦桥路368)"
    elif re.match('^hkg',host):
        cur_location = "香港数据中心"
    elif re.match('zhibu-sz-',host):
        cur_location = "中信证券深圳南方机房"
    else:
        cur_location = "公司（九江路501号）"

    return cur_location


def update_servers(datas):
    for i in datas:
        if re.match("[A-Z6].{9}$", i):
            for j in live_info.my_hosts:
                if live_info.get_seri(j) == i :
                    if datas[i]["HostName"] != j:
                        print "{} hostname changed from {} to {}".format(i, datas[i]["HostName"], j)
                        datas[i]["HostName"] = j

                    if datas[i]["NICS"] != live_info.get_nic_ip_mac(j):
                        print "{} {} NICS changed from {} to {}".format(i,datas[i]["HostName"],datas[i]["NICS"],live_info.get_nic_ip_mac(j))
                        datas[i]["NICS"] = live_info.get_nic_ip_mac(j)

        # update the current location
        datas[i]['cur_location'] = get_cur_location(datas[i]["HostName"])


if __name__ == "__main__":
    hosts_dir=["live-out", "hub_out", "output"]
    live_info = readlive.ReadLiveInfo(hosts_dir)

    with codecs.open("server_detail.yml", 'r', "utf-8") as f:
        datas = yaml.safe_load(f,)

    update_servers(datas)
    with open("server_detail.yml",'w') as f:
        yaml.safe_dump(datas, f, allow_unicode=True)

    # reload the updated server_detail.yml file
    with codecs.open("server_detail.yml", 'r', "utf-8") as f:
        new_datas = yaml.safe_load(f,)

    for i in new_datas:
        with codecs.open('conf/{}'.format(i), 'w',encoding="utf-8") as jf:
            json.dump(new_datas[i], jf, ensure_ascii=False)

