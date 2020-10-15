#!/usr/bin/env python3

import time
import sys
import argparse
import subprocess
import influxdb

def getSnmp(username,auth,authpass,privpass,host, oid):
    cmd = 'snmpbulkwalk -v3 -l authPriv -u {} -a {} -A \'{}\' -x aes -X \'{}\' {} {}'.format(username,auth,authpass,privpass,host,oid)
    try:
        output = subprocess.check_output(cmd,shell=True,timeout=5)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf-8'))
        sys.exit(e.returncode)
    
    output = output.decode('utf-8')
    return output.strip().split('\n')

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

def ifIndex_map_ifDescr(username, auth, authpass, privpass, host):
    ifdescr_oid = '1.3.6.1.2.1.2.2.1.2'
    ifdescr = getSnmp(username, auth, authpass, privpass, host, ifdescr_oid)
    ifname_map = {}
    for i in ifdescr:
        ifname_map[i.split('=')[0].strip().split('.')[-1]] = i.split('=')[1].split()[-1]
    
    return ifname_map

def main(username, auth, authpass, privpass, host):
    ifname_map = ifIndex_map_ifDescr(username, auth, authpass, privpass, host)

    mroutetable_oid = '1.3.6.1.2.1.83.1.1.2.1'
    mroutetable = getSnmp(username,auth,authpass,privpass,host, mroutetable_oid)
    
    nexthop_oid = '1.3.6.1.2.1.83.1.1.3.1'
    outgoingtable = getSnmp(username,auth,authpass,privpass,host, nexthop_oid)

    mroutetable_subindex_map = {
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
        key = i.split(mroutetable_oid[-10:])[1].split('=')[0].strip().split('.')[1]
        group = '.'.join(i.split(mroutetable_oid[-10:])[1].split('=')[0].strip().split('.')[2:6])
        source = '.'.join(i.split(mroutetable_oid[-10:])[1].split('=')[0].strip().split('.')[6:10])
        mask = '.'.join(i.split(mroutetable_oid[-10:])[1].split('=')[0].strip().split('.')[10:14])
        value = ' '.join(i.split(mroutetable_oid[-10:])[1].split('=')[1].strip().split()[1:])
        if key=='5':
            if value == '0':
                value = 'None'
            else:
                value = ifname_map[value]

        group_id = '{}.{}.{}'.format(group, source, mask)

        if group_id not in group_infos:
            group_infos[group_id] = { 'ipMrouteGroup': group, 'ipMRouteSource': source, 'ipMRouteSourceMask': mask }   

        group_infos[group_id][mroutetable_subindex_map[key]] = value
    
    
    for i in outgoingtable:
        group = '.'.join(i.split(nexthop_oid[-10:])[1].split('=')[0].strip().split('.')[2:6])
        source = '.'.join(i.split(nexthop_oid[-10:])[1].split('=')[0].strip().split('.')[6:10])
        mask = '.'.join(i.split(nexthop_oid[-10:])[1].split('=')[0].strip().split('.')[10:14])
        OutInterface = ifname_map[i.split(nexthop_oid[-10:])[1].strip().split('=')[0].split('.')[14]]
        group_id = '{}.{}.{}'.format(group, source, mask)
        if 'OutInterfaces' not in group_infos[group_id]:
            group_infos[group_id]['OutInterfaces'] = OutInterface
        else:
            if OutInterface not in group_infos[group_id]['OutInterfaces']:
                group_infos[group_id]['OutInterfaces'] += ' {}'.format(OutInterface)
    
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
    main(args.user, args.auth, args.authpass, args.privpass, args.host)