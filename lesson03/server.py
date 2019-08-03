#!/usr/bin/env python

import json, subprocess, argparse, os, sys
from socket import *
import time


def time_server(args):
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind(('', args.port))           # Присваивает порт 8888
    s.listen(5)                       # Переходит в режим ожидания запросов;
                                      # одновременно обслуживает не более
                                      # 5 запросов.
    print("Time Server on port {} has been created. Awaiting for connections!".format(args.port))

    while True:
        client, addr = s.accept()     # Принять запрос на соединение
        print("Received connection from {}".format(str(addr)))
        timestr = time.ctime(time.time()) + "\n"
        client.send(timestr.encode('ascii'))
        client.close()


def main(args):
    time_server(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p','--port',
        type=int,
        default=7777,
        help='Server Connection Port')
    parser.add_argument('-c','--config',
        type=str,
        default='config.yml',
        help='Config File Full Path')
    args = parser.parse_args()

    main(args)
