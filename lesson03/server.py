#!/usr/bin/env python

from socket import *
import helpers
from helpers import args

LISTENERS = 5


class Server:
    def __init__(self, addr, port):
        # TODO: apply address usage
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


def main():
    console_args = helpers.args()
    s = Server(console_args.addr, console_args.port)
    s.create()


if __name__ == '__main__':
    main()
