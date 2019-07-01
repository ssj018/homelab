#-*-coding:utf-8-*-
import json
import subprocess
import readcsv
import regex as re
import yaml
import sys


def ReadFormDirs(dir):
    cmd = 'ls {}'.format(dir)
    files = subprocess.check_output(cmd, shell=True)
    myhosts = {}
    for file in files.split():
        with open('{}/{}'.format(dir, file),'r') as f:
            myhosts[file] = json.load(f)

    return myhosts

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
        ciy1host = ['ciytradea1','ciytradea2','ciytradea3','ciytradea4','ciytrip1','ciyquote1','ciydatalog']
        if host in ciy1host:
            cur_location = "中信期货移动机房一期（宁桥路600号）"
        else:
            cur_location = "中信期货移动机房二期（宁桥路500号）"
    elif re.match("zeus5|mdstrademon[34]|pfsense-hubdc",host):
        cur_location = "hub dc (秦桥路368)"
    else:
        cur_location = "公司（九江路501号）"

    return  cur_location

def suppermicro_seri_match(serino):
    pattern = '^[A-Z][A-Z0-9]{14}$'
    return re.match(re.compile(pattern), serino)


def get_nic_ip_mac(host):
    interfaces = host['ansible_facts'].get('ansible_interfaces')
    devices = {}
    ips = {}
    macs = {}
    nics_info = {}
    for i in interfaces:
        device = "ansible_" + i
        devices[i] = host['ansible_facts'].get(device, {})
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


def get_seri(host):
    return host['ansible_facts']['ansible_product_serial']


def get_productName(host):
    return host["ansible_facts"]["ansible_product_name"]


def get_info_by_hostname(hostname,hosts):
    print hostname.lower()
    for i in hosts:
        if hostname.lower() == i:
            NICS = get_nic_ip_mac(hosts[hostname.lower()])
            ProductName = get_productName(hosts[hostname.lower()])
            return NICS, ProductName


def gen_server_info(seri,it_name, Status,nics_info,Price,HostName, productname, buy_date, tg, size):
    server_detail_info = {}
    server_detail_info[seri] = {
        "it_name": it_name,
        "Status": Status,
        "NICS": nics_info,
        "price": Price,
        "HostName": HostName,
        "ProductName": productname,
        "buy_date": buy_date,
        "tg": tg,
        "size": size
    }
    return server_detail_info


if __name__ == "__main__":
    csv_file = 'file/test123.csv'
    csv_osoa_file = 'file/124.csv'

    # get online hosts from ansible setup module
    hosts_dir = ["live-out", "hub_out", "output"]
    my_hosts = {}
    for i in hosts_dir:
        my_hosts.update(ReadFormDirs(i))

    # get one server one account servers
    osoa_host_data = readcsv.loadcsv(csv_osoa_file)
    osoa_host = readcsv.parseosoadata(osoa_host_data)
    

    OnlineSeriNo = []
    for i in my_hosts:
        OnlineSeriNo.append(get_seri(my_hosts[i]))

    osoa_info = {}
    for i in osoa_host.keys():
        ser = get_seri(my_hosts[i])
        productname = get_productName(my_hosts[i])
        nics_info = get_nic_ip_mac(my_hosts[i])
        Status = "online"
        Price = "74500"
        buy_date = "2018/5/30"
        it_name = i
        HostName = i
        osoa_info[ser] = {
             "it_name": it_name,
             "Status": Status,
             "NICS": nics_info,
             "price": Price,
             "HostName": HostName,
             "ProductName": productname,
             "buy_date": buy_date,
             "tg": {"2019/6/5": {"location": "中信期货移动二期机房", "account_name":osoa_host[i]}},
             "size": "1U惠普-整机购买"
             }

    # get servers record in csv files 
    data = readcsv.loadcsv(csv_file)
    pdata = readcsv.parsedata(data)

    #add one server one account servers to  record
    pdata.update(osoa_info)

    #get details for record servers
    for i in pdata:
        # fix pfsense server
        if i == 'CN77070CYV':
            pfsense_nics= {
                "bge0": "10.100.1.2/9c:dc:71:be:60:98",
              "bge1": "220.248.102.162/9c:dc:71:be:60:99",
               "bge2": "10.1.10.1/9c:dc:71:be:60:9a",

            }
            tg = {}
            size = '1U惠普-整机购买'
            pdata.update(gen_server_info(i, "pfsense", "online", pfsense_nics, "20210", "pfsense", "HP Product DL360", "2018/1/22", tg, size))
            continue

        if i == 'CN783805LH':
            pfsense_hub_nics= {
                "bge0": "211.147.95.190/20:67:7c:e2:07:f4",
              "bge1": "192.168.1.1/20:67:7c:e2:07:f5",

            }
            tg = {}
            size = '1U惠普-整机购买'
            pdata.update(gen_server_info(i, "pfsense-hubdc", "online", pfsense_hub_nics, "21250", "pfsense-hubdc", "HP Product DL360", "2018/3/5", tg, size))
            continue

        # supermicro servers
        if i not in OnlineSeriNo:
            if suppermicro_seri_match(i):
                super_it_name = super_hostname = pdata[i]["it_name"]
                super_price = pdata[i]["price"]
                super_tg = pdata[i]["tg"]
                super_buy_date = pdata[i]["buy_date"]
                super_size = pdata[i]["size"]
                out = subprocess.Popen("ping -c2 {}".format(super_hostname),shell=True,stdout=subprocess.PIPE)
                out.communicate()
                if out.returncode == 0:
                    super_nics, super_product_name = get_info_by_hostname(super_hostname, my_hosts)
                    pdata.update(gen_server_info(i, super_it_name, "online", super_nics,super_price,super_hostname, super_product_name, super_buy_date, super_tg, super_size))
                    continue
                pdata.update(gen_server_info(i, super_it_name, "offline", "None", super_price, "none", "super server",super_buy_date, super_tg, super_size))
                continue

        # hp servers
        for j in my_hosts:
            if i == get_seri(my_hosts[j]):
                pdata[i]["HostName"] = j
                pdata[i]["NICS"] = get_nic_ip_mac(my_hosts[j])
                pdata[i]["Status"] = 'online'
                pdata[i]["ProductName"] = get_productName(my_hosts[j])
                break
                
     # add current location
    for i in pdata:
        try:
             cur_locaton = get_cur_location(pdata[i]['HostName'])
             pdata[i]["cur_location"] = cur_locaton
        except Exception as e:
            print i
            print e.message
            sys.exit(1)

    # for i in pdata:
    #    with open('conf/{}'.format(i), 'w') as f:
    #        json.dump(pdata[i], f, ensure_ascii=False)

    with open("server_detail.yml",'w') as f:
        yaml.safe_dump(pdata,f,allow_unicode=True)
