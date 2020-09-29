#!/usr/bin/env python3

import sys
from pysnmp.entity.rfc3413.oneliner import cmdgen
from influxdb import InfluxDBClient
import argparse
from pysnmp.hlapi import UsmUserData, usmHMACMD5AuthProtocol, usmHMACSHAAuthProtocol, usmAesCfb128Protocol

def ifIndexMapToifDesc(host, userData, index):
    # '''
    #   Oid_info:
    #     ifIndex: 1.3.6.1.2.1.2.2.1.1  (tables)
    #     ifDescr: 1.3.6.1.2.1.2.2.1.2  (tables)
    #  '''
    ifnamemap = {}
    Index_oid = '1.3.6.1.2.1.2.2.1.1'
    Descr_oid = '1.3.6.1.2.1.2.2.1.2'
    Index_resp = getBulkSnmp(host,userData, OID=Index_oid) # get ifIndex
    Descr_resp = getBulkSnmp(host, userData, OID=Descr_oid) # get ifDescr (ifname)

    for i in Index_resp:
        for  j  in  Descr_resp:
            if i[0].__str__().split('=')[1].strip() == j[0].__str__().split('=')[0].split('.')[-1].strip():
                ifnamemap[i[0].__str__().split('=')[1].strip()] = j[0].__str__().split('=')[1].strip()
                break
        else:
            print('index: {} has not matched name'.format(i[0].__str__().split('=')[1]))

    return ifnamemap[index]

def getBulkSnmp(host, userData, OID, port=161):
    '''
     getBulkSnmp for tables oid request
    '''

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.bulkCmd(userData,cmdgen.UdpTransportTarget((host,port)),0,25,OID)

    if errorIndication:
	    print(errorIndication)
    elif errorStatus:
        print('{} at {}'.format(errorStatus.prettyPrint(),errorindex and varBindTable[int(errorindex)-1][0] or '?'))
    
    if not varBindTable or 'No Such Object available on this agent at this OID' in varBindTable[0]:
        print('No Such Object available on this agent at this OID on switch: {}'.format(host))
        sys.exit(1)

    return varBindTable

def formatSnmp(mroutetable, host, userData):
    oid = '1.3.6.1.2.1.83.1.1.2.1'
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
    mgroup_name_map = {
        '239.255.101.104': 'mcastnetlogagin',
        '239.3.3.3.2': 'test'
    }
    sourceip_hostname_map = {
        '0.0.0.0' : 'None-source',
        '10.1.89.251' : 'systool'
    }
    mroutetableEntries = []
    group_infos = {}
    for  i in mroutetable:
        key = i[0].__str__().split(oid[-7:])[1].split('=')[0].split('.')[1]
        group = '.'.join(i[0].__str__().split(oid[-7:])[1].split('=')[0].split('.')[2:6])
        source = '.'.join(i[0].__str__().split(oid[-7:])[1].split('=')[0].split('.')[6:10]).strip()
        mask = '.'.join(i[0].__str__().split(oid[-7:])[1].split('=')[0].split('.')[10:14]).strip()
        value = i[0].__str__().split(oid[-7:])[1].split('=')[1].strip()

        if group not  in  mgroup_name_map:
            groupname = 'unkowngroup'
        else:
            groupname = mgroup_name_map[group]

        if source not in  sourceip_hostname_map:
            sourcehostname = 'unkownsource'
        else:
            sourcehostname = sourceip_hostname_map[source]

        if key == '5':
            if value == '0':
                value = '0({})'.format('None')
            else:
                value = ifIndexMapToifDesc(host,userData,value)

        group_id = '{}.{}.{}'.format(group, source, mask)
        if group_id not in group_infos:
            group_infos[group_id] = { 'ipMrouteGroup': '{}({})'.format(group, groupname), 'ipMRouteSource': '{}({})'.format(source,sourcehostname), 'ipMRouteSourceMask': mask, }   

        group_infos[group_id][subindex_map[key]] = value
    
    for  i in group_infos:
        mroutetableEntries .append({'host': host, 'mrouteEntry_id': i, 'mrouteEntry_detail' : group_infos[i]})
    
    return mroutetableEntries

def writeinfluxdb(dbhost,dbname, dbuser, dbuser_passord, data, port=8086):
    client = InfluxDBClient(host=dbhost, database=dbname,username=dbuser, password=dbuser_passord, port=port)
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

def main(host, userdata):
    host = host
    # community = 'mds'
    mroutetable_oid = '1.3.6.1.2.1.83.1.1.2.1'
    mroutetable = getBulkSnmp(host, userdata, mroutetable_oid)
    mroutetableEntries = formatSnmp(mroutetable, host, userdata)
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
    if args.auth == 'md5':
        authProtocol = usmHMACMD5AuthProtocol
    else:
        authProtocol = usmHMACSHAAuthProtocol

    userdata = UsmUserData(args.user, args.authpass, args.privpass, authProtocol=authProtocol, privProtocol=usmAesCfb128Protocol)
    main(args.host, userdata)
