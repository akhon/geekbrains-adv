import pytest
from helpers import *


def test_parser():
    sys.argv = ['-p 7777', '-c', 'config.yml', '-a', 'testhost']
    console_args = args()
    assert console_args.port == 7777
    assert console_args.addr == 'testhost'
    assert console_args.config == 'config.yml'

def test_config():
    config = Config()
    assert config.get_port() == 7777
    assert config.get_addr() == ''
    assert config.get_buffersize() == 1024
