#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Karl.Lv@outlook.com, KarlLv@126.com
# 18 August, 2017

import sys

def readfile(filename):
    '''Print a file to the :standard out.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

"""
print "sys.argv[0]--------", sys.argv[0]
print "sys.argv[1]--------", sys.argv[1]
print "sys.argv[2]--------", sys.argv[2]
"""

# Script starts from here

if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()


if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # Fetch sys.argv[1] but without the first 2 characters
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''
        This program prints files to the standard output.
        Any number of files can be specified.
        Options include:
        --version   : Print the version number
        --help      : Display this help'''
    else:
        print 'Unknown option.'
else:
    for filename in sys.argv[1:]:
        readfile(filename)
