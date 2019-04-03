import pytest
import socket
import requests

def check_is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    return result == 0

def test_connection():
    assert check_is_open('localhost', 49152)

def test_get_graphiql():
    response = requests.get('http://localhost:49152/static/graphiql')
    assert response.status_code == 200
