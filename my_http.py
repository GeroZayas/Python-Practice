from http.server import HTTPServer, BaseHTTPRequestHandler
from random import choice


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, Gero")


httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
