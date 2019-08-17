# import pytest
# from datetime import datetime
#
# from protocol import make_response
#
#
# @pytest.fixture
# def initial_action():
#     return 'presence'
#
#
# @pytest.fixture
# def initial_code():
#     return 200
#
#
# def test_action_create_server():
#     console_args = args()
#     config = Config(console_args.addr, console_args.port, console_args.bufsize)
#     if console_args.config:
#         config.read_configfile(console_args.config)
#
#     s = Server(config.get_config())
#     s.create()
#     actual_response = make_response(initial_request, initial_code, initial_data)
#     assert actual_response.get('action') == initial_action
#
#
# def test_code_make_response(initial_request, initial_code, initial_data):
#     actual_response = make_response(initial_request, initial_code, initial_data)
#     assert actual_response.get('code') == initial_code
#
#
# def test_data_make_response(initial_request, initial_code, initial_data):
#     actual_response = make_response(initial_request, initial_code, initial_data)
#     assert actual_response.get('data') == initial_data
