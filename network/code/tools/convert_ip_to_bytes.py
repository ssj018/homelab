import struct

def convert_ip_to_bytes(ip):
    sections = ip.split('.')
    Bytes_IP = struct.pack('>4B', int(sections[0]), int(sections[1]), int(sections[2]), int(sections[3]))
    return  Bytes_IP

if __name__ == "__main__":
    b_ip = convert_ip_to_bytes('192.168.1.1')
    print(b_ip)