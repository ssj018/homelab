import struct

def convert_ip_to_bytes(ip):
    sections = list(map(lambda x: int(x), ip.split('.')))
    Bytes_IP = struct.pack('>4B', sections[0], sections[1], sections[2], sections[3])
    return  Bytes_IP

if __name__ == "__main__":
    b_ip = convert_ip_to_bytes('192.168.1.1')
    print(b_ip)