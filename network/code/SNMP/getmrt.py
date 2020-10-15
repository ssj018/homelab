#!/usr/bin/env python3

import time
import sys
import argparse
import subprocess
import influxdb

def calctimes(func):
    def innner(*args, **kwags):
        start = time.time()
        result = func(*args, **kwags)
        end = time.time()
        used_time = end - start
        print('{} used {} seconds'.format(func.__name__, used_time))
        return result
    
    return innner

@calctimes    
def getSnmp(username,auth,authpass,privpass,host, oid):
    cmd = 'snmpbulkwalk -v3 -l authPriv -u {} -a {} -A \'{}\' -x aes -X \'{}\' {} {}'.format(username,auth,authpass,privpass,host,oid)
    # print(cmd)
    try:
        output = subprocess.check_output(cmd,shell=True,timeout=5)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))
        sys.exit(e.returncode)
    
    output = output.decode('utf-8')
    return output.strip().split('\n')


@calctimes
def writeinfluxdb(dbhost,dbname, dbuser, dbuser_passord, data, port=8086):
    client = influxdb.InfluxDBClient(host=dbhost, database=dbname,username=dbuser, password=dbuser_passord, port=port)
    fields = { "mrouteEntry_id": data['mrouteEntry_id'] }
    fields.update(data['mrouteEntry_detail'])
    json_body = [
        {
            "measurement": "snmp_mroutetable",
            "tags": {
                "host": data['host'],     
            },
            'fields' : fields

        }
    ]
    client.write_points(json_body)

def main(username, auth, authpass, privpass, host,oid):
    mroutetable = getSnmp(username,auth,authpass,privpass,host, oid)
    subindex_map = {
        '1': 'ipMRouteGroup',
        '2': 'ipMRouteSource',
        '3': 'ipMRouteSourceMask',
        '4': 'ipMRouteUpstreamNeighbor',
        '5': 'ipMRoteInIfIndex',
        '6': 'ipMRouteUpTime',
        '7': 'ipMRouteExpiryTime',
        '8': 'ipMRoutePkts',
        '9': 'ipMRouteDifferentInIfPackets',
        '10': 'ipMRouteOctets',
        '11': 'ipMRouteProtocol',
        '12': 'ipMRouteRtProto',
        '13': 'ipMRouteRtAddress',
        '14': 'ipMRouteRtMask',
        '15': 'ipMRouteRtType',
        '16': 'ipMRouteHCOctets'
    }

    mroutetableEntries = []
    group_infos = {}
    for  i in mroutetable:
        key = i.split(oid[-7:])[1].split('=')[0].split('.')[1]
        group = '.'.join(i.split(oid[-7:])[1].split('=')[0].split('.')[2:6])
        source = '.'.join(i.split(oid[-7:])[1].split('=')[0].split('.')[6:10]).strip()
        mask = '.'.join(i.split(oid[-7:])[1].split('=')[0].split('.')[10:14]).strip()
        value = ' '.join(i.split(oid[-7:])[1].split('=')[1].strip().split()[1:])
        if key=='5':
            if value == '0':
                value = 'None'
            else:
                # print(group,source)
                interface_oid ='1.3.6.1.2.1.2.2.1.2.{}'.format(value)
                value = getSnmp(username, auth, authpass, privpass, host, interface_oid)[0].split('=')[-1].split()[-1]

        group_id = '{}.{}.{}'.format(group, source, mask)
        if group_id not in group_infos:
            group_infos[group_id] = { 'ipMrouteGroup': '{}({})'.format(group, group), 'ipMRouteSource': '{}({})'.format(source,source), 'ipMRouteSourceMask': mask, }   

        group_infos[group_id][subindex_map[key]] = value
    
    for  i in group_infos:
        mroutetableEntries .append({'host': host, 'mrouteEntry_id': i, 'mrouteEntry_detail' : group_infos[i]})

    
    for i  in  mroutetableEntries:
        writeinfluxdb('10.1.77.99','mroutes','admin', 'password', i)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument('--host','-H', required=True, help='IP or hostname of the devices')
    parse.add_argument('--user','-u', required=True, help='User name of snmp v3')
    parse.add_argument('--authpass', '-p', required=True, help='auth password of snmp v3 user')
    parse.add_argument('--privpass', '-P', required=True, help='priv password of snmp v3 user')
    parse.add_argument('--auth', '-a', default='sha', choices=['sha','md5'])
    args = parse.parse_args()
    mroutetable_oid = '1.3.6.1.2.1.83.1.1.2.1'
    main(args.user, args.auth, args.authpass, args.privpass, args.host, mroutetable_oid)