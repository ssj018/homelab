import subprocess
import re

def os_cmd_output(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print("failed message", e)
        exit(1)
    return output

def get_mac(iface):
    data=os_cmd_output('ifconfig {}'.format(iface))
    mac_address=re.findall(b"\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w", data)
    return mac_address[0].decode()

if __name__ == "__main__":
    mac=get_mac('eth1')
    print(mac)