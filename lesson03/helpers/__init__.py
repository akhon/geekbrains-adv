import argparse
import os, sys


config = {
    'host': 'localhost',
    'port': 7777
}


def args():
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('-p', '--port',
                        type=int,
                        default=7777,
                        help='Server Connection Port')
    parser.add_argument('-a', '--addr',
                        type=str,
                        default='localhost',
                        help='Server Hostname/IP-address')
    parser.add_argument('-c', '--config',
                        type=str,
                        default='config.yml',
                        help='Config File Full Path')
    return parser.parse_args()
