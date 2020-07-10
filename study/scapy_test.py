#/usr/bin/env python3
from scapy.all import * 

ip = Ether(src='00:00:00:00:00:01')/IP(dst='127.0.0.1', frag=1)/ICMP()

print(ip.show())