import pytest
import socket

def check_is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    return result == 0


def test_connection():
    assert check_is_open('localhost', 8080)
