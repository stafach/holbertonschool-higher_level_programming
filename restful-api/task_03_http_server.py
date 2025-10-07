#!/usr/bin/env python3
"""
this module use http.server module for implementing web servers
"""


from http.server import BaseHTTPRequestHandler
import socketserver


class my_server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")


PORT = 8000

with socketserver.TCPServer(("", PORT), my_server) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
