import socket
import ssl

server_key = 'cert/server.key'
server_cert = 'cert/server.crt'
def startserver(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen(5)
    ssl_s = ssl.wrap_socket(s,keyfile=server_key ,certfile=server_cert ,server_side=True, ca_certs='cert/ca.crt')
    try:
        while True:
            conn, addr = ssl_s.accept()
            rdata = b''
            while True:
                data = conn.recv(2048)
                if not data:
                    print('{} has send data: {}'.format(addr, rdata.decode(encoding='utf-8')))
                    break
                rdata += data
    except KeyboardInterrupt:
        print('Server quit!')
        ssl_s.close()


def startserver2(address, port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert/server.crt', 'cert/server.key')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen(5)
    ssl_s = context.wrap_socket(s, server_side=True)
    try:
        while True:
            conn, addr = ssl_s.accept()
            rdata = b''
            while True:
                data = conn.recv(2048)
                if not data:
                    print('{} has send data: {}'.format(addr, rdata.decode(encoding='utf-8')))
                    break
                rdata += data
    except KeyboardInterrupt:
        print('Server quit!')
        ssl_s.close()


if __name__ == "__main__":
    startserver2('localhost', 9999)