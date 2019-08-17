import pytest
from helpers import *


@pytest.fixture()
def initial_action():
    return 'presence'


@pytest.fixture()
def initial_type():
    return 'status'


@pytest.fixture()
def initial_username():
    return 'TestUsername'


@pytest.fixture()
def initial_status():
    return 'Yep, I am here!'


@pytest.fixture()
def initial_user(initial_username, initial_status):
    return {'account_name': initial_username, 'status': initial_status}


def test_jim(initial_action, initial_type, initial_username):
    expanded_msg = JimMessage(action=initial_action, time=time(), type=initial_type, user=initial_username).expand()
    assert expanded_msg.get('action') == initial_action
    assert expanded_msg.get('type') == initial_type
    assert expanded_msg.get('user') == initial_username
