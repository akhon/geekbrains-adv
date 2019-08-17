import pytest


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
