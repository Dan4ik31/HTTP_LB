import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "127.0.0.1"
serverPort = 8888
requestList = {}

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()

        response = ''
        for key in requestList:
            response += '{0}: {1}\n'.format(key, requestList[key])
        self.wfile.write(bytes(response, "utf-8"))

    def do_POST(self):
        length = int(self.headers['Content-length'])
        requestList[datetime.datetime.now()] = self.rfile.read1(length).decode()

if __name__ == "__main__":
    httpServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        httpServer.serve_forever()
    except KeyboardInterrupt:
        pass

    httpServer.server_close()
