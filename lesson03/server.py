#!/usr/bin/env python

from socket import *
from time import gmtime
import pickle
import helpers


class Server:
    def __init__(self, addr, port):
        # TODO: apply address usage
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)


    def craft_reply(self, msg):
        if msg['action'] == 'presence':
            reply = {
                "response": 200,
                "time": gmtime()
            }
        else:
            reply = {
                "response": 400,
                "time": gmtime()
            }
        return pickle.dumps(reply)


    def send_reply(self, client, reply):
        client.send(reply)
        return


    def receive_message(self, client, addr):
        msg = pickle.loads(client.recv(1000000))
        print('Received message: {} from client: {}'.format(msg, addr))
        return msg


    def create(self):
        try:
            self.socket.bind(('', self.port))
            self.socket.listen(helpers.LISTENERS)

            print('Echo Server on {}:{} has been created. Awaiting for connections!'.format(self.addr, self.port))
            while True:
                client, addr = self.socket.accept()
                msg = self.receive_message(client, addr)
                reply = self.craft_reply(msg)
                self.send_reply(client, reply)
                client.close()
        except Exception as e:
            print(e)


def main():
    console_args = helpers.args()
    s = Server(console_args.addr, console_args.port)
    s.create()


if __name__ == '__main__':
    main()
