#!/usr/bin/env python

import pickle
import logging
from socket import *
from helpers import *


class Server:
    def __init__(self, config):
        self.addr = config['addr']
        self.port = config['port']
        self.buffersize = config['buffersize']
        self.socket = socket(AF_INET, SOCK_STREAM)

    def craft_reply(self, msg):
        # only one reply for now
        if msg['action'] == 'presence':
            reply = JimMessage(response=200, time=time())
        else:
            reply = JimMessage(response=400, time=time())
        return pickle.dumps(reply.expand())

    def send_reply(self, client, reply):
        client.send(reply)
        return

    def receive_message(self, client, addr):
        msg = pickle.loads(client.recv(MESSAGE_SIZE))
        print('Received message: {} from client: {}'.format(msg, addr))
        return msg

    def shutdown(self):
        self.socket.close()
        print('Graceful Shutdown')

    def create(self):
        try:
            self.socket.bind((self.addr, self.port))
            self.socket.listen(LISTENERS)

            print('JiM Server on {}:{} has been created. Awaiting for connections!'.format(self.addr, self.port))
            while True:
                client, addr = self.socket.accept()
                msg = self.receive_message(client, addr)
                reply = self.craft_reply(msg)
                self.send_reply(client, reply)
                client.close()

        except KeyboardInterrupt:
                self.shutdown()

        except Exception as e:
            print(e)


def main():
    console_args = args()
    config = Config(console_args.addr, console_args.port, console_args.bufsize)
    if console_args.config:
        config.read_configfile(console_args.config)

    s = Server(config.get_config())
    s.create()


if __name__ == '__main__':
    main()
