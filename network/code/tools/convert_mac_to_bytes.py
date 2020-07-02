import struct
def hex_to_int(hexstr):
    return int(hexstr,16)

def Str_to_Int(string):
    hex_list=string.split(":")
    int_list=map(hex_to_int,hex_list)
    return int_list

def convert_mac_bytes(mac):
    sections =list(Str_to_Int(mac))
    mac_bytes = struct.pack('!6B', sections [0], sections [1], sections [2], sections [3], sections [4], sections [5])
    return mac_bytes

if __name__ == "__main__":
    #mac=convert_mac_bytes('40:8d:5c:11:fa:1d')
   # print(mac)
    #print(b'40:8d:5c:11:fa:1d')
    # a=Str_to_Int('40:8d:5c:11:fa:1d')
    # print(list(a))
    mac_bytes = convert_mac_bytes('40:8d:5c:11:fa:1d')
    print(mac_bytes)