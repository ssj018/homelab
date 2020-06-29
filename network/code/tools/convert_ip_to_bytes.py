import struct

def convert_ip_to_bytes(ip):
    sections = ip.split('.')
    print(sections)

if __name__ == "__main__":
    convert_ip_to_bytes('192.168.1.1')