#!/usr/bin/env python

import pickle
import yaml
from socket import *
from helpers import *


class Server:
    def __init__(self, addr, port, configfile=None):
        self.addr = addr
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)

        if configfile:
            with open(configfile) as file:
                file_config = yaml.safe_load(file)
                config.update(file_config or {})

            file.close()

            try:
                self.addr, self.port = config.get('host'), config.get('port')
            except Exception as e:
                print('ERROR: Problem with loading parameters from config file')
                print(e)
                exit(1)

        if self.addr:
            config['host'] = self.addr
        if self.port:
            config['port'] = self.port


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

    def create(self):
        try:
            self.socket.bind((self.addr, self.port))
            self.socket.listen(LISTENERS)

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
    console_args = args()
    s = Server(console_args.addr, console_args.port)
    s.create()


if __name__ == '__main__':
    main()
