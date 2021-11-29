# Python 3 server
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

hostName = "localhost"
serverPort = 8080
dt_info = datetime.datetime.today().strftime("%A, %d %B %Y, %H:%M:%S")


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
        log = dt_info + ': ' + request_text
        with open("register.log", "a") as file:
            file.write(log + '\n')
        file.close()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    start_server = "Server started http://%s:%s" % (hostName, serverPort)
    print(start_server)

    with open("register.log", "a") as file:
        file.write(dt_info + ' - ' + start_server + '\n')
    file.close()

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
