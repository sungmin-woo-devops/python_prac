from http.server import HTTPServer, BaseHTTPRequestHandler
import time

# HOST = "127.0.0.1"    # localhost, 127.0.0.1로 접속됨 / 192.168.0.17로 안됨
# Private IP와 Localhost 둘다 서버 접속에 사용 가능하게 하려면 어떻게 해야하는가?
HOST = "192.168.0.17"  # localhost 또는 127.0.0.1로 접속 안됨 Why?
PORT = 9998

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>","utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))
        #self.wfile.write(bytes(f'\{"time": "{date}"\}', "utf-8"))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server is now Running...")
server.serve_forever()
server.server_close()
print("Server is closed...")
