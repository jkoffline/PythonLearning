#!/usr/bin/env python3
# -*- utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
#
# 3 July, 2017
#
# python -m http.server
#
# python -m http.server 8000
#


import sys
import locale
import http.server
import socketserver

def main(argv):
    if len(sys.argv) < 3:
        print("Usage: python3 python_httpser_1.py <host IP> <port>")
        exit()
    elif (len(sys.argv) == 3):
        addr = sys.argv[1]
        port = locale.atoi(sys.argv[2])

        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer((addr, port), handler)
        print("HTTP serve is at: http://%s:%d/" % (addr, port))
        httpd.serve_forever()
    else:
        print("Parameters exceeds 3")

if __name__ == '__main__':
    main(sys.argv)
