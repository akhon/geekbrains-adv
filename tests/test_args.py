import pytest
from helpers import *


@pytest.fixture()
def initial_port():
    return 7777


@pytest.fixture()
def initial_addr():
    return ''


@pytest.fixture()
def initial_buffersize():
    return 1024


@pytest.fixture()
def initial_configfile():
    return 'config.yml'


@pytest.fixture()
def initial_args(initial_addr, initial_port, initial_buffersize, initial_configfile):
    return ['-a {}'.format(initial_addr), '-p {}'.format(initial_port), '-b {}'.format(initial_buffersize), '-c',
            initial_configfile]


def test_parser(initial_args, initial_addr, initial_port, initial_buffersize, initial_configfile):
    sys.argv = initial_args
    console_args = args()
    assert console_args.addr == initial_addr
    assert console_args.port == initial_port
    assert console_args.bufsize == initial_buffersize
    assert console_args.config == initial_configfile


def test_config(initial_addr, initial_port, initial_buffersize, initial_configfile):
    config = Config()
    config.read_configfile(initial_configfile)
    assert config.get_addr() == initial_addr
    assert config.get_port() == initial_port
    assert config.get_buffersize() == initial_buffersize

