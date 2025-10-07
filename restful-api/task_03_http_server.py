#!/usr/bin/env python3
"""
this module use http.server module for implementing web servers.
Create a subclass of BaseHTTPRequestHandler who implement GET
"""


import http.server
import json


class my_server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            reponse = json.dumps(sample_data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(reponse.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            sample_info = {
                "version": 1.0,
                "description": "A simple API built with http.server"
            }
            info = json.dumps(sample_info)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(info.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"page not found sorry")


PORT = 8000

httpd = http.server.HTTPServer(("", PORT), my_server)
print("serving at port", PORT)
httpd.serve_forever()
