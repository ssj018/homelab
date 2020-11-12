#!/usr/bin/env python3
import yaml
import prettytable as pt

gh = {}
with open('/home/sunsj/vscode/homelab/mds_formatgroups/groups', 'r') as f:
    lines = f.readlines()

for i  in  lines:
    if i.split()[3] not in gh:
        gh[i.split()[3]] = [i.split()[2]]
    gh[i.split()[3]].append(i.split()[2])

with open('/home/sunsj/vscode/homelab/mds_formatgroups/main.yml', 'r') as f:
    gn = yaml.safe_load(f)
    
for i  in gn['mcast_hosts']:
    print(i)


tb = pt.PrettyTable()
tb.field_names = ["group", "name", "colos"]   
for i  in gh:
    for j in  gn['mcast_hosts']:
        if i == j['ip']:
            name = j['domain']
            break
    else:
        name = 'unknown'
    tb.add_row([i, name, gh[i]])

print(tb)
