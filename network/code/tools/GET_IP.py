import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,  # SIOCGIFADDR
    struct.pack('256s', (ifname[:15]).encode()))[20:24])


if __name__ == "__main__":
 #   print('eth1'[:15].encode())
    print((struct.pack('256s', ('eth1'[:15]).encode()))[20:24])
 #   print(get_ip_address('eth1'))