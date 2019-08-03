#!/usr/bin/env python3

from socket import *
from time import time
import pickle
import helpers


class Client:
    def __init__(self, addr, port, name):
        self.name = name
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)


    def connect(self):
        try:
            self.socket.connect((self.addr, self.port))
            print("Successfully connected to {}:{}".format(self.addr, self.port))
        except Exception as e:
            print(e)

        self.send(self.craft_presense())


    def craft_presense(self):
        # TODO: move into Message class
        msg = {
            'action': 'presence',
            'time': time(),
            'type': 'status',
            'user': {
                'account_name': self.name,
                'status': 'Yep, I am here!'
            }
        }
        return pickle.dumps(msg)


    def send(self, msg):
        self.socket.send(bytes(msg))


    def receive(self):
        return self.socket.recv(1024)


    def parse(self, msg):
        return msg.decode('ascii')


    def close(self):
        self.socket.close()


    def whoami(self):
        return self.name


def main():
    console_args = helpers.args()
    c = Client(console_args.addr, console_args.port, 'Skywalker')
    c.connect()
    c.close()


if __name__ == '__main__':
    main()
