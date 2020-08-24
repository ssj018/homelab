import socket
import ssl

def startclient(server, port):
    try:
        while True:
            msg = input('Enter:')
            print(msg)
            msg = msg.encode(encoding='utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='cert/ca.crt')
            client.connect((server, port))
            client.sendall(msg)
            client.close() 
    except KeyboardInterrupt:
        print('close ...')
        client.close() 

def startclient2(server, port):
    ctx = ssl.create_default_context()
    ctx.load_verify_locations('cert/ca.crt')
    ctx.check_hostname = False
    try:
        while True:
            msg = input('Enter:')
            print(msg)
            msg = msg.encode(encoding='utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client = ctx.wrap_socket(s)
            client.connect((server, port))
            client.sendall(msg)
            client.close() 
    except KeyboardInterrupt:
        print('close ...')
        client.close() 

if __name__ == "__main__":
    startclient2('localhost', 9999)