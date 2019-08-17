import argparse
import os, sys, yaml
from time import time

MESSAGE_SIZE = 1024
LISTENERS = 5
DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S +0000"

# use from http import HTTPStatus?
error_codes = {
    100: 'Basic Notification',
    101: 'Important Notification',
    200: 'OK',
    201: 'Object Created',
    202: 'Confirm',
    400: 'Bad Request',
    401: 'Auth Required',
    402: 'Auth Failure',
    403: 'Forbidden',
    404: 'Not Found',
    409: 'Auth Conflict',
    410: 'User Offline',
    500: 'Server Error'
}

class Config:
    def __init__(self, addr='', port=7777, buffersize=1024):
        self.config = {
            'addr': addr,
            'port': port,
            'buffersize': buffersize
        }

    def read_configfile(self, configfile):
        if configfile:
            with open(configfile) as file:
                file_config = yaml.safe_load(file)
            file.close()

            if file_config:
                try:
                    self.config.update(file_config)
                except Exception as e:
                    print('ERROR: Problem with loading parameters from config file')
                    print(e)
                    exit(1)

    def get_config(self):
        return self.config

    def get_port(self):
        return self.config['port']

    def get_addr(self):
        return self.config['addr']

    def get_buffersize(self):
        return self.config['buffersize']


class JimMessage:
    def __init__(self, **kwargs):
        self.raw = kwargs
        self.raw['time'] = time()

    @property
    def action(self):
        return self.raw.get('action', None)

    @property
    def response(self):
        return self.raw.get('response', None)

    @property
    def get_username(self):
        return self.raw['user'].get('account_name', None) if 'user' in self.raw else None

    @property
    def get_recipient(self):
        return self.raw.get('to', None)

    @property
    def get_sender(self):
        return self.raw.get('from', None)

    @property
    def get_message(self):
        return self.raw.get('message', None)

    def expand(self):
        return self.raw


def args():
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p', '--port',
                        type=int,
                        default=7777,
                        help='Server Connection Port')
    parser.add_argument('-a', '--addr',
                        type=str,
                        default='',
                        help='Server Hostname/IP-address')
    parser.add_argument('-b', '--bufsize',
                        type=int,
                        default=1024,
                        help='Buffer Size')
    parser.add_argument('-c', '--config',
                        type=str,
                        default='',
                        help='Use config file instead of vars')
    return parser.parse_args()
