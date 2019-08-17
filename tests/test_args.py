import pytest
from helpers import *
from . import initial_addr, initial_port, initial_buffersize, initial_configfile


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
