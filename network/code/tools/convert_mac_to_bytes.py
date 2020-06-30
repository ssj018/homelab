import struct

def Str_to_Int(string):
    print(ord(string[0]))

def convert_mac_bytes(mac):
    mac_str = ''.join(mac.split(":"))
    print(mac_str)
    mac_bytes = bytes.fromhex(mac_str)
    return mac_bytes

if __name__ == "__main__":
    mac=convert_mac_bytes('40:8d:5c:11:fa:1d')
    print(mac)
    print(b'40:8d:5c:11:fa:1d')