import socket
import fcntl
import struct

def get_mac_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ##inet_ntoa()功能是将网络地址转换成“.”点隔的字符串格式。
    #
    # ioctl(fd, cmd, args)
    #fcntl.ioctl(s.fileno(),0x8927, struct.pack('256s', (ifname[:15]).encode()))
    #第一个参数： 传入socket文件描述符 
    #第二个参数： 指定操作，（0x8927获取MAC的指令）
    #第三个参数： 一个内存区域（个人理解，一段固定格式的bytes类型的数据，），通常根据第二参数的指令确定需要的格式，网络相关操作一般是：struct ifreq / struct ifconf 两种
    #struct ifreq
    # 这个结构定义在include/net/if.h，用来配置ip地址，激活接口，配置MTU等接口信息的
    #struct ifreq {
    #     char ifr_name[IFNAMSIZ]; /* Interface name */
    #     union {
    #         struct sockaddr ifr_addr;
    #         struct sockaddr ifr_dstaddr;
    #         struct sockaddr ifr_broadaddr;
    #         struct sockaddr ifr_netmask;
    #         struct sockaddr ifr_hwaddr;
    #         short           ifr_flags;
    #         int             ifr_ifindex;
    #         int             ifr_metric;
    #         int             ifr_mtu;
    #         struct ifmap    ifr_map;
    #         char            ifr_slave[IFNAMSIZ];
    #         char            ifr_newname[IFNAMSIZ];
    #         char           *ifr_data;
    #     };
    # };
    #操作 SIOCGIFADDR 返回的结果也是 struct ifreq 结构体。其中，网卡的 IPv4 地址信息包含在 struct sockaddr ifr_addr 结构体内。
    # 这个 4 字节的 IP 地址位于 struct ifreq 结构体 20-23 字节处。
    # 所以我们会看到，fcntl.ioctl 返回的结果后面有 [18:24] ——只需要把这 6 个字节拿去转换就可以了。
    mac_bytes = fcntl.ioctl(s.fileno(),0x8927,  struct.pack('256s', (ifname[:15]).encode()))[18:24]
  
    return ":".join([ '%02x'%i for  i in mac_bytes])

if __name__ == "__main__":
    print(get_mac_address('eth1'))