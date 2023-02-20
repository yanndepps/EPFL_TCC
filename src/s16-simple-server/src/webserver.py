# A simple web server
# ---

import http.server
import socketserver

port = 8000
handler = http.server.SimpleHTTPRequestHandler

my_web_server = socketserver.TCPServer(("", port), handler)

print("start listening to port " + str(port))
my_web_server.serve_forever()
