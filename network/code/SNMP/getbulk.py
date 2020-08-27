#!/usr/bin/env python3

from pysnmp.entity.rfc3413.oneliner import cmdgen
import pysnmp.smi.rfc1902

def getBulkSnmp(host, community, port=161, OID='1.3.6.1.2.1.2.2.1.2'):
    snmp_respon = []
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.bulkCmd(cmdgen.CommunityData(community),cmdgen.UdpTransportTarget((host,port)),0,25,OID)

    if errorIndication:
	    print(errorIndication)
    elif errorStatus:
        print('{} at {}'.format(errorStatus.prettyPrint(),errorindex and varBindTable[int(errorindex)-1][0] or '?'))

    for varBindTableRow in varBindTable:
	    for i in varBindTableRow:
		    snmp_respon.append(i.__str__())
    
    return snmp_respon

    
if __name__ == "__main__":
    resp = getBulkSnmp('10.1.10.2','mds',OID='1.3.6.1.2.1.83.1.1.2.1')
    print(resp)