import csv
macs = []
with open('Mac-whitelist-of-wifi.csv', 'r') as f:
    sp = csv.reader(f, delimiter=' ', quotechar='|')
    for row in  sp:
        macs.append(row)
        print(row)

print(macs)