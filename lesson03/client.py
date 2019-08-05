#!/usr/bin/env python3

import pickle
from socket import *
from time import time, strftime, localtime
from helpers import *


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

        # crafting presense message and sending to the server
        self.send(self.craft_presense())
        response = self.receive()
        self.parse(pickle.loads(response))

    def craft_presense(self):
        msg = JimMessage(action='presence', time=time(), type='status', user={'account_name': self.name, 'status': 'Yep, I am here!'})
        return pickle.dumps(msg.expand())

    # send in bytes
    def send(self, msg):
        self.socket.send(bytes(msg))

    # receive in bytes
    def receive(self):
        return self.socket.recv(MESSAGE_SIZE)

    def parse(self, msg):
        if msg['response'] in error_codes:
            print('Server response {}:{} at {}'.format(msg['response'], error_codes[msg['response']], strftime(DATE_TIME_FORMAT, localtime(msg['time']))))
        else:
            print('Something went wrong')

    def close(self):
        self.socket.close()

    def whoami(self):
        return self.name


def main():
    console_args = args()
    c = Client(console_args.addr, console_args.port, 'Skywalker')
    c.connect()
    c.close()


if __name__ == '__main__':
    main()
