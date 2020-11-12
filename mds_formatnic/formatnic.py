#!/usr/bin/env python3
import re
import math

with open('1', 'r') as f:
   lines = f.readlines()

head=True
nic_info = {}
for i in lines:
    if i == '\n':
        head=True
    else:
        if head:
            servername = i.split()[0]
            nic_info[servername] = []
            head = False
        else:
            nic_info[servername] += [i]

print('<html>\n<table border="1">')
print("<tr><td>")
print("Hostname")
print("</td><td>")
print('Nics Info')
print("</td><td>")
print("Numbers of  Non-X5 nics")
print("</td></tr>")
cnts = 0
for i  in nic_info:
    if re.match('ciyconn.*|wks.*', i):
        continue
    cnt = 0
    print('<tr>\n<td>\n')
    print(i)
    print('</td>\n<td>')
    print('<table>')
    for nic in  nic_info[i]: 
        print('<tr><td>')
        print(nic)
        print('</td></tr>')
        if 'ConnectX-5' not in nic:
            cnt += 1
    print('</table>\n</td>\n<td>')
    tcnt = math.ceil(cnt/2)
    print(tcnt)
    print('</td>\n</tr>')
    cnts += tcnt
print('<tr><td>')
print('Total Non-X5 nics:')
print('</td><td>')
print(cnts)
print('</td></tr>')
print('</table>\n</html>') 
