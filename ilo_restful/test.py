import urllib3
import requests.packages
import argparse
import json
import yaml
import sys
import pprint

urllib3.disable_warnings()
auth = ('administrator','passw0rd')
headers = {'content-type': 'application/json'}

def get_ilo_version(host):
    url = "https://{}/rest/v1".format(host)
    r = requests.get(url,auth=auth,headers=headers,verify=False)
    pprint.pprint(r.json())
    if 'Hp' in r.json()['Oem']:
        return r.json()['Oem']['Hp']['Manager'][0]['ManagerType']
    return  r.json()['Oem']['Hpe']['Manager'][0]['ManagerType']



def get_ilo_yml(host,workload,ex_url):
    url = "https://{}{}".format(host, ex_url)
    r = requests.get(url, auth=auth, headers=headers, verify=False)
    ret = r.json()
    with open('bios/config_{}_{}.yml'.format(host,workload),'w') as f:
        yaml.safe_dump(ret,f)


def patch_bios(host,conf,ex_url):
    with open(conf,'r') as f:
        config=yaml.safe_load(f)

    url = "https://{}{}".format(host, ex_url)
    data = json.dumps(config)
    try:
        r = requests.patch(url, data, auth=auth, headers=headers, verify=False)
        print "Bios update success!! You need to restart your server manually"
    except:
        print "failed to patch bios"

def put_bios(host,conf,ex_url):
    with open(conf,'r') as f:
        config=yaml.safe_load(f)

    url = "https://{}{}".format(host, ex_url)
    data = json.dumps(config)
    try:
        r = requests.put(url, data, auth=auth, headers=headers, verify=False)
        print "Bios put success!! You need to restart your server manually"
    except:
        print "failed to put bios"


if __name__== "__main__":
    parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument('-i', '--host',  help='the dest host', required=True)
    parse.add_argument('-a', '--action',  help='choose your action', choices=['get_version','get_yml','patch','put'], required=True)
    parse.add_argument('-u', '--url', help='url of restful api', required=True)
    parse.add_argument('-c', '--conf', help='patch conf ')
    parse.add_argument('-w', '--workload', help='workload of bios ',default='custom')
    args = parse.parse_args()
    
    if args.action == 'get_yml':
        get_ilo_yml(args.host,args.workload ,args.url)
    if args.action == 'get_version':
       print(get_ilo_version(args.host))
    if args.action == 'patch':
        if not  args.conf:
            print "no patch conf file"
            sys.exit(1)
        patch_bios(args.host,args.conf, args.url)
    if args.action == 'put':
        if not  args.conf:
            print "no put conf file"
            sys.exit(1)
        put_bios(args.host,args.conf,args.url)
