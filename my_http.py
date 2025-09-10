from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, Gero\n")
        self.wfile.write(b"Hello, Again\n")
        self.wfile.write("<h1>Hello, Again</h1>\n")


httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
