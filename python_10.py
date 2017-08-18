#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Karl.Lv@outlook.com, KarlLv@126.com
# March 17, 2017

# Get MAC address, hostname, and IP address

import uuid
import socket

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    print mac
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


mymac = get_mac_address()

myhostname = socket.gethostname()

print myhostname

myname = socket.getfqdn(socket.gethostname())

myaddr = socket.gethostbyname(myname)

print mymac

print myname

print myaddr
