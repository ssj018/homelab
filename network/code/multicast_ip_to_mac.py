# --coding: utf-8--

import time
import socket

def list_all_mcast_ipaddress():
    for s1 in range(224,240):
        for s2 in range(0,256):
            for s3 in range(0,256):
                for s4 in range(0,256):
                    mip = '{}.{}.{}.{}'.format(s1,s2,s3,s4)
                    yield mip

def translate_ip_int_to_binary(ip):
    ip_sec = ip.split('.')
    ipbinary_sec=[]
    for i in ip_sec:
        ipbinary_sec.append('{:08b}'.format(int(i)))
    return '-'.join(ipbinary_sec)

def translate_multicastip_to_multicastmac(mcastip):
    # prefix of multicast macaddress  
    mcast_mac_prefix = '00000001-00000000-01011110-0'
    mac_mcast_sec = []
    if int(mcastip.split('.')[0]) in range(224,240):
        # get last 23 bit of multicast ip address
        mac_binary = mcast_mac_prefix + translate_ip_int_to_binary(mcastip)[-25:]
        for i in mac_binary.split('-'):
            mac_mcast_sec.append(hex(int(i,2)).encode('utf-8'))
        mac_mcast_humen = ['%02x' % int(i,16) for i in mac_mcast_sec]
        print(mcastip, '-'.join(mac_mcast_humen)) 
    else:
        print('{} is not a mcast ip'.format(mcastip))
    


if __name__ == '__main__':
    mips = list_all_mcast_ipaddress()
    for i in mips:
    #     print(' {}\t{}'.format(i,translate_ip_int_to_binary(i)))
    #     time.sleep(1)
        translate_multicastip_to_multicastmac(i)