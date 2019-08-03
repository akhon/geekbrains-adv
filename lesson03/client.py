#!/usr/bin/env python3

from socket import *
from console import args


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
        # {
        #     "action": "presence",
        #     "time": time.time()
        #     "type": "status",
        #     "user": {
        #         "account_name": "C0deMaver1ck",
        #         "status": "Yep, I am here!"
        #     }
        # }


    def craft(self, msg):
        return msg.encode('utf-8')


    def send(self):
        self.socket(msg)


    def receive(self):
        return self.socket.recv(1024)


    def parse(self, msg):
        return msg.decode('ascii')


    def close(self):
        self.socket.close()


    def whoami(self):
        return self.name


def main():
    console_args = args()
    c = Client(console_args.addr, console_args.port, 'Skywalker')
    c.connect()
    print(c.whoami())
    c.close()


if __name__ == '__main__':
    main()
