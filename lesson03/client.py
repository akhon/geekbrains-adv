#!/usr/bin/env python3

import argparse, os, sys
from socket import *


def craft_message(msg):
    return msg.encode('utf-8')


def send_message(sock, msg):
    sock.send(craft_message(msg))
    return


def receive_message(s):
    return parse_message(s.recv(1024))


def parse_message(msg):
    return msg.decode('ascii')


def connect(args):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((args.addr, args.port))
    msg = 'test'
    send_message(s, msg)
    t_msg = receive_message(s)
    s.close()
    print("Current time is {}".format(t_msg))


def main(args):
    connect(args)


if __name__ == '__main__':
    # argparser
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p','--port',
                        type=int,
                        default=7777,
                        help='Server Connection Port')
    parser.add_argument('-a','--addr',
                        type=str,
                        default='localhost',
                        help='Server Hostname/IP-address')
    parser.add_argument('-c','--config',
                        type=str,
                        default='config.yml',
                        help='Config File Full Path')
    args = parser.parse_args()

    main(args)
