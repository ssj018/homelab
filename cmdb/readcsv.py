# -*- coding: utf-8 -*-
import csv
import json
from pprint import pprint


def loadcsv(file):
    data=[]
    with open(file) as f :
        rows = csv.DictReader(f)
        for row in rows:
            data.append(row)
    return data


def parsedata(data):
    post_data = {}
    key = ''
    for row in data:
        if row['产品编号'] is not '':
            key = row['产品编号']
            post_data[key] = {
                'buy_date': row['购买日期'],
                'size': row['机型'],
                'price': row['购买价格'],
                'it_name': row['IT名称'],
                'HostName': "None",
                'NICS': "None",
                "Status": "offline",
                "ProductName":"unknown",
                'tg': {row['时间']: {'location': row['机房/机柜'], 'account_name': row['托管主体']}}}
        temp_dict = {row['时间']: {'location': row['机房/机柜'], 'account_name': row['托管主体']}}
        post_data[key]['tg'].update(temp_dict)

    return post_data


def parseosoadata(data):
    osoa_host = {}
    for row in data:
        if row["主机名"] != "":
            osoa_host[row["主机名"]] = row["﻿托管主体"]

    return osoa_host




if __name__ == '__main__':
    data = loadcsv('file/124.csv')
    host = parseosoadata(data)
    print(host)
    # pdata = parsedata(data)
    # with open('yml_conf/all.yml', 'w') as f:
    #         yaml.dump(pdata, f,allow_unicode=True)
    # for i in pdata:
    #    with open('conf/{}'.format(i), 'w') as f:
    #        json.dump(pdata[i], f, ensure_ascii=False)
