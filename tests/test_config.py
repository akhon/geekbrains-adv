from helpers import *
from . import initial_addr, initial_port, initial_buffersize, initial_configfile


def test_config(initial_addr, initial_port, initial_buffersize, initial_configfile):
    config = Config()
    config.read_configfile(initial_configfile)
    assert config.get_addr() == initial_addr
    assert config.get_port() == initial_port
    assert config.get_buffersize() == initial_buffersize