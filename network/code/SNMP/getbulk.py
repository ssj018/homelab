#!/usr/bin/env python3

from pysnmp.entity.rfc3413.oneliner import cmdgen
import pysnmp.smi.rfc1902
import pprint
import prettytable as pt

class SwitchesMrouteEntries:
    def __init__(self, key, group, mask, source, value):
        self.key = key
        self.group = group
        self.source = source
        self.mask = mask
        self.value = value

    def __str__(self):
        return '{}.{}.{}.{} = {}'.format(self.key, self.group, self.source, self.mask, self.value)



def ifIndexMapToifDesc(host, community):
    # '''
    #   Oid_info:
    #     ifIndex: 1.3.6.1.2.1.2.2.1.1  (tables)
    #     ifDescr: 1.3.6.1.2.1.2.2.1.2  (tables)
    #  '''
    ifnamemap = {}
    Index_oid = '1.3.6.1.2.1.2.2.1.1'
    Descr_oid = '1.3.6.1.2.1.2.2.1.2'
    Index_resp = getBulkSnmp(host, community, OID=Index_oid) # get ifIndex
    Descr_resp = getBulkSnmp(host, community, OID=Descr_oid) # get ifDescr (ifname)

    for i in Index_resp:
        for  j  in  Descr_resp:
            if i[0].__str__().split('=')[1].strip() == j[0].__str__().split('=')[0].split('.')[-1].strip():
                ifnamemap[i[0].__str__().split('=')[1].strip()] = j[0].__str__().split('=')[1].strip()
                break
        else:
            print('index: {} has not matched name'.format(i[0].__str__().split('=')[1]))

    return ifnamemap


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

    return varBindTable

def getnextSnmp(host, community, OID, port=161 ):
    '''
     get Snmp for single-point oid request
    '''
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(cmdgen.CommunityData(community),cmdgen.UdpTransportTarget((host,port)),OID)

    if errorIndication:
	    print(errorIndication)
    elif errorStatus:
        print('{} at {}'.format(errorStatus.prettyPrint(),errorindex and varBindTable[int(errorindex)-1][0] or '?'))
     
    return varBindTable

def getSnmp(host, community, OID, port=161 ):
    '''
     get Snmp for single-point oid request
    '''
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.getCmd(cmdgen.CommunityData(community),cmdgen.UdpTransportTarget((host,port)),OID)

    if errorIndication:
	    print(errorIndication)
    elif errorStatus:
        print('{} at {}'.format(errorStatus.prettyPrint(),errorindex and varBindTable[int(errorindex)-1][0] or '?'))
     
    return varBindTable
    
def showmroutetables(entries_list):
    tables = {}
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
    for i  in entries_list:
        if i.key not in tables:
            tb = pt.PrettyTable()
            tb.field_names = ['ipMRouteGroup', 'ipMRouteSource', 'ipMRouteSourceMask', subindex_map[i.key]]
            tables[i.key] = tb

    for i in entries_list:
        tables[i.key].add_row([i.group, i.source, i.mask, i.value])

    return tables
    

def main():
    host = '10.1.10.2'
    community = 'mds'
    mtables = {}
    mroutetable_oid = '1.3.6.1.2.1.83.1.1.2.1'
    mroutetable = getBulkSnmp(host, community, mroutetable_oid)
    mtables = []
    for  i in mroutetable:
        key = i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[1]
        group = '.'.join(i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[2:6])
        source = '.'.join(i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[6:10]).strip()
        mask = '.'.join(i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[0].split('.')[10:14]).strip()
        value = i[0].__str__().split(mroutetable_oid[-7:])[1].split('=')[1].strip()
        mtables.append(SwitchesMrouteEntries(key, group, mask, source, value))
   
    tables = showmroutetables(mtables)
    for i  in tables:
        print(tables[i])
         


if __name__ == "__main__":
    # resp = getBulkSnmp('10.1.48.6','mds',OID='1.3.6.1.2.1.2.2.1.2')
    # for  i  in  resp:
        # print(i)
    # namemap = ifIndexMapToifDesc('10.1.48.6','mds')
    # print(namemap['10114'])
    # resp1 = getSnmp('10.1.48.6','mds',OID='1.3.6.1.2.1.2.2.1.2.5002')
    # resp = getBulkSnmp('10.1.48.6','mds',OID='1.3.6.1.2.1.2.2.1.2')
    # print(resp1[0])
    # for  i in resp:
    #     print(i[0])
    main()
    # resp = getBulkSnmp('10.1.10.2','mds',OID='1.3.6.1.2.1.83.1.1.2.1')
    # for i in resp:
    #     print(i[0])
    