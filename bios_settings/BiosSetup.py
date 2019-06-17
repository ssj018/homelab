#!/usr/bin/env python

import urllib3
import requests
import argparse
import json
import yaml
import sys
import pprint

urllib3.disable_warnings()
auth = ('Administrator', 'passw0rd')
headers = {
    'content-type': 'application/json',
          }


def create_login_session(host):
    data = {
        'UserName': 'administrator',
        'Password': 'passw0rd'
    }
    data = json.dumps(data)
    session_url = 'https://{}/redfish/v1/Sessions'.format(host)
    try:
        r = requests.post(session_url, data=data, headers=headers, verify=False)
        return r.headers['X-Auth-Token'], r.headers['Location']
    except:
        print "failed to create login session"
        sys.exit(1)


def get_sessions(host):
    XAuthToken, Location = create_login_session(host)
    headers["X-Auth-Token"] = XAuthToken
    print headers
    session_url = 'https://{}/redfish/v1/Sessions'.format(host)
    r = requests.get(session_url,  headers=headers, verify=False)
    for i in r.json()['Members']:
        print i['@odata.id']


def del_sessions(host, XAuthToken,Location):
    headers["X-Auth-Token"] = XAuthToken
    ret = requests.delete(Location,headers=headers, verify=False)
    if ret.status_code == 200:
        print "deleted the session :{}".format(Location)
    else:
        print "failed to delete session: {}".format(Location)


def get_ilo_version(host):
    BaseInfoUrl = "https://{}/rest/v1".format(host)
    try:
        r = requests.get(BaseInfoUrl, auth=auth, headers=headers, verify=False)
        r.headers
    except:
        print "failed to get ilo info of {}".format(host)
        sys.exit(1)

    if 'Hp' in r.json()['Oem']:
        return r.json()['Oem']['Hp']['Manager'][0]['ManagerType']
    return r.json()['Oem']['Hpe']['Manager'][0]['ManagerType']


def get_current_bios(host):
    XAuthToken,Location = create_login_session(host)
    headers["X-Auth-Token"] = XAuthToken
    BiosSettingsUrl = '/redfish/v1/Systems/1/bios'
    url = "https://{}{}".format(host, BiosSettingsUrl)

    r = requests.get(url, headers=headers, verify=False)
    with open('bios/config_{}.yml'.format(host), 'w') as f:
        yaml.safe_dump(r.json(), f)

    del_sessions(host,XAuthToken,Location)


def patch_bios(host, conf):
    with open(conf, 'r') as f:
        config = yaml.safe_load(f)
    BiosSettingsUrl = '/rest/v1/Systems/1/bios/Settings'
    url = "https://{}{}".format(host, BiosSettingsUrl)
    data = json.dumps(config)
    r = requests.patch(url, data, auth=auth, headers=headers, verify=False)
    if r.status_code == 200:
        print "Bios update success!! You need to restart your server manually"
    else:
        print "failed to patch bios"
        print r.headers
        print r.status_code
        sys.exit(1)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument('-i', '--host', help='the dest host', required=True)
    parse.add_argument('-p', '--patch', action='store_true', default=False, help="Specify whether to update the BIOS")
    args = parse.parse_args()

    #get_sessions(args.host)
    #del_old_sessions(args.host)
    #del_sessions(args.host)
    #create_login_session(args.host)
    get_current_bios(args.host)
    #ilo_version = get_ilo_version(args.host)

    # print ilo_version
    if args.patch and ilo_version == "iLO 5":
        patch_bios(args.host, "conf/HP_G10_BIOS_PATCH.yml")
    if args.patch and ilo_version == "iLO 4":
        patch_bios(args.host, "conf/HP_G9_BIOS_PATCH.yml")
