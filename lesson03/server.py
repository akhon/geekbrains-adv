#!/usr/bin/env python

import argparse, os, sys
from socket import *

LISTENERS = 5


class Server:
    def __init__(self, addr, port):
        # TODO: apply address
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)


    def craft_message(self, msg):
        return msg.encode('utf-8')


    def send_message(self, client, msg):
        client.send(self.craft_message(msg))
        return


    def receive_message(self, client, addr):
        msg = client.recv(1000000).decode('utf-8')
        print('Received message: {} from client: {}'.format(msg, addr))
        return msg


    def create(self):
        try:
            self.socket.bind(('', self.port))
            self.socket.listen(LISTENERS)

            print('Echo Server on {}:{} has been created. Awaiting for connections!'.format(self.addr, self.port))
            while True:
                client, addr = self.socket.accept()
                msg = self.receive_message(client, addr)
                self.send_message(client, msg)
                client.close()
        except Exception as e:
            print(e)


def main(args):
    s = Server(args.addr, args.port)
    s.create()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p','--port',
                        type=int,
                        default=7777,
                        help='Server Connection Port')
    parser.add_argument('-a', '--addr',
                        type=str,
                        default='localhost',
                        help='Server Address')
    parser.add_argument('-c','--config',
                        type=str,
                        default='config.yml',
                        help='Config File Full Path')
    args = parser.parse_args()

    main(args)
