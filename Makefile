SHELL = /bin/sh

CC = gcc

format_string: format_string.c
	gcc -m32 format_string.c -o format_string -fstack-protector -fpic -fpic -pie -Wl,-z,now -Wl,-z,relro
