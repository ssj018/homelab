#!/usr/bin/env python3

import sys
from pysnmp.entity.rfc3413.oneliner import cmdgen
import pysnmp.smi.rfc1902
import pprint
import prettytable as pt
from influxdb import InfluxDBClient

class SwitchesMrouteEntries:
    def __init__(self, hostname, group_info, value, snmptype):
        self.hostname = hostname
        self.group_info = group_info
        self.value = value
        self.snmptype = snmptype

    def __str__(self):
        return '{}.{}.{} = {}'.format(self.hostname, self.snmptype, self.group_info, self.value)


def getBulkSnmp(host, community, OID, port=161):
    '''
     getBulkSnmp for tables oid request
    '''

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.bulkCmd(cmdgen.CommunityData(community),cmdgen.UdpTransportTarget((host,port)),0,25,OID)

    if errorIndication:
	    print(errorIndication)
    elif errorStatus:
        print('{} at {}'.format(errorStatus.prettyPrint(),errorindex and varBindTable[int(errorindex)-1][0] or '?'))
    
    if not varBindTable or 'No Such Object available on this agent at this OID' in varBindTable[0]:
        print('No Such Object available on this agent at this OID on switch: {}'.format(host))
        sys.exit(1)

    return varBindTable


def writeinfluxdb(dbhost,dbname, dbuser, dbuser_passord, data, port=8086):
    client = InfluxDBClient(host=dbhost, database=dbname,username=dbuser, password=dbuser_passord, port=port)
    json_body = [
        {
            "measurement": "snmp_mroutetable",
            "tags": {
                "host": data.hostname,
                "type": data.snmptype,
                "group_info": data.group_info
            },
            "fields": {
                "value": data.value
            }

        }
    ]

    client.write_points(json_body)

def main(host):
    host = host
    community = 'mds'
    mtables = {}
    mroutetable_oid = '1.3.6.1.2.1.83.1.1.2.1'
    mroutetable = getBulkSnmp(host, community, mroutetable_oid)
    mtables = []
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
    for  i in mroutetable:
        key = i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[1]
        group_info = '.'.join(i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[2:14]).strip()
        value = i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[1].strip()
        mtables.append(SwitchesMrouteEntries(host, group_info, value, subindex_map[key]))
   
    for i  in mtables:
        print(i)
        writeinfluxdb('10.1.77.99','test','admin', 'password', i )







if __name__ == "__main__":
    main('10.1.48.6')

    