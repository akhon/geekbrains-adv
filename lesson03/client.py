#!/usr/bin/env python3

import json, subprocess, argparse, os, sys
from socket import *


def get_server_time(args):
    s = socket(AF_INET,SOCK_STREAM)  # Создать сокет TCP
    s.connect((args.server, args.port))   # Соединиться с сервером
    tm = s.recv(1024)                # Принять не более 1024 байтов данных
    s.close()
    print("Current time is {}".format(tm.decode('ascii')))


def main(args):
    get_server_time(args)


if __name__ == '__main__':
    # argparser
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p','--port',
        type=int,
        default=7777,
        help='Server Connection Port')
    parser.add_argument('-s','--server',
        type=str,
        default='localhost',
        help='Server Hostname/IP-address')
    parser.add_argument('-c','--config',
        type=str,
        default='config.yml',
        help='Config File Full Path')
    args = parser.parse_args()

    main(args)
