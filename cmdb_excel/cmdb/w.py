import subprocess

cmd='cd /opt/cmdb/;ansible-cmdb -C cols/cust_ser.conf out_ser/ '

output = subprocess.check_output(cmd, shell=True)

print output
print ["\xe6\x9c\xba\xe6\x88\xbf"]
