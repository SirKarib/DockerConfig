# Python 3 server
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
import os

hostName = "localhost"
serverPort = 8080
DT_INFO = datetime.datetime.today().strftime("%A, %d %B %Y, %H:%M:%S")
LOG_PATH = os.getenv("LOG_PATH", "/log/web-server/register.log")


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>http://127.0.0.1/serv/</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        if self.path != "/favicon.ico":
            self.write_logs()
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def write_logs(self):
        request_text = self.path
        log = DT_INFO + ': ' + request_text
        with open(LOG_PATH, "a") as file:
            file.write(log + '\n')
        file.close()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    START_SERVER = "Server started http://%s:%s" % (hostName, serverPort)
    print(START_SERVER)

    with open(LOG_PATH, "a") as file:
        file.write(DT_INFO + ' - ' + START_SERVER + '\n')
    file.close()

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    STOP_SERVER = "Server stopped."
    print(STOP_SERVER)

    with open(LOG_PATH, "a") as file:
        file.write(DT_INFO + ' - ' + STOP_SERVER + '\n')
    file.close()
