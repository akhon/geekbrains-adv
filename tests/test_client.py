from helpers import *
from client import Client
from . import *


@pytest.fixture()
def tcp_server(initial_addr, initial_port, initial_tcp_server_listeners):
    import socket

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((initial_addr, initial_port))
    tcp_socket.listen(initial_tcp_server_listeners)

    return tcp_socket


def test_client(initial_addr, initial_port, initial_buffersize, initial_username, tcp_server):
    config = Config(initial_addr, initial_port, initial_buffersize)
    c = Client(config.get_config(), initial_username)
    assert c.whoami() == initial_username
    # assert c.craft_presense()
    # assert c.parse()
    # assert c.connect()
    # assert c.close()
    # assert c.send()
    tcp_server.close()
