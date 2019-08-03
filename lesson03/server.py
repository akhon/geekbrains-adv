#!/usr/bin/env python

import argparse, os, sys
from socket import *


def craft_message(msg):
    return msg.encode('utf-8')


def send_message(sock, msg):
    sock.send(craft_message(msg))
    return


def receive_message(sock, addr):
    msg = sock.recv(1000000).decode('utf-8')
    print('Received message: {} from client: {}'.format(msg, addr))
    return msg


def echo_server(args):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', args.port))
    s.listen(5)

    print('Echo Server on port {} has been created. Awaiting for connections!'.format(args.port))
    while True:
        client, addr = s.accept()
        msg = receive_message(client, addr)
        send_message(client, msg)
        client.close()


def main(args):
    echo_server(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p','--port',
                        type=int,
                        default=7777,
                        help='Server Connection Port')
    parser.add_argument('-a', '--addr',
                        type=str,
                        default='config.yml',
                        help='Server Address')
    parser.add_argument('-c','--config',
                        type=str,
                        default='config.yml',
                        help='Config File Full Path')
    args = parser.parse_args()

    main(args)
