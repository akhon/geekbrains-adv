import threading

from helpers import *
from client import Client
from server import Server
from . import *


@pytest.fixture(autouse=True)
def tcp_server(initial_addr, initial_port, initial_tcp_server_listeners):
    config = Config(initial_addr, initial_port, initial_buffersize)
    s = Server(config.get_config())
    thread = threading.Thread(target=s.create)
    thread.daemon = True
    thread.start()


def test_client(initial_addr, initial_port, initial_buffersize, initial_username):
    config = Config(initial_addr, initial_port, initial_buffersize)
    c = Client(config.get_config(), initial_username)
    assert c.whoami() == initial_username
    assert c.connect() == True
    c.close()
