import http.server
import ssl

Handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(('localhost', 4443), Handler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='cert/server.key', certfile='cert/server.crt', server_side=True)

httpd.serve_forever()