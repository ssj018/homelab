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
    BaseInfoUrl = "https://{}/rest/v1".format(host)
    r = requests.get(BaseInfoUrl,auth=auth,headers=headers,verify=False)
    pprint.pprint(r.json())
    if 'Hp' in r.json()['Oem']:
        return r.json()['Oem']['Hp']['Manager'][0]['ManagerType']
    return  r.json()['Oem']['Hpe']['Manager'][0]['ManagerType']


def patch_bios(host,conf):
    with open(conf,'r') as f:
        config=yaml.safe_load(f)
    BiosSettingsUrl = '/rest/v1/Systems/1/bios/Settings'
    url = "https://{}{}".format(host, BiosSettingsUrl)
    data = json.dumps(config)
    try:
        r = requests.patch(url, data, auth=auth, headers=headers, verify=False)
        print "Bios update success!! You need to restart your server manually"
    except:
        print "failed to patch bios"
        sys.exit(1)

if __name__== "__main__":
    parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument('-i', '--host',  help='the dest host', required=True)
    args = parse.parse_args()
    
    ilo_version=(get_ilo_version(args.host))
    print ilo_version
    if ilo_version == "iLO 5":
        patch_bios(args.host,"conf/HP_G10_BIOS_PATCH.yml")
    if ilo_version == "iLO 4":
        patch_bios(args.host,"conf/HP_G9_BIOS_PATCH.yml")

