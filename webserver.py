#!/usr/bin/env python
#

import SimpleHTTPServer
import SocketServer

PORT = 8080

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), handler)

print "Serving at port", PORT

httpd.serve_forever()
