#!/usr/bin/env python3
import re
import sys
import time
import socket

# hostname = sys.argv[1]
# port = int(sys.argv[2])

_host = '188.130.155.66'

def outputparser(out):
    ret = re.search("Next port:(\d+)", out)
    if ret:
        return ret.group(1)
    return None

def netcat(h, p):
    print("Netcat to %s %i" % (h, p))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((h,p))

    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    print("Connection closed.")
    sock.close()
    return outputparser(res)

def start():
    for i in range(46470, 46480):
        ret = netcat(_host, i)
        if ret:
            return ret

def main():
    next_port = start()
    while True:
        if next_port:
            next_port = netcat(_host, int(next_port))
        else:
            break

if __name__ == '__main__':
    main()
