#/usr/bin/env python3
from scapy.all import * 

send = Ether()/ARP(pdst='10.1.16.1')

print(send.show())
# receivepacket, sendpacket = srp(send, timeout=1)
print(sendp(send))
# print(receivepacket[0][1].op,receivepacket[0][1].hwsrc) 