#!/usr/bin/env python3

import sys

def help():
    print("Usage: {} {{number of %x}}".format(sys.argv[0]))
    exit(1)

if len(sys.argv) < 2:
    help()

num = int(sys.argv[1])

output = 'A'*4 + 'B'*4 + ' '
output += ''.join(['%x ' for i in range(num)])

print(output, end='')
