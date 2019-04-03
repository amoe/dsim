import pytest
import socket
import requests

def check_is_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    return result == 0

def wait_until_open(host, port, timeout):
    elapsed = 0
    while not check_is_open(host, port):
        time.sleep(1)
        elapsed += 1
        if elapsed > timeout:
            raise Exception('timed out waiting for server to come up')
    return elapsed

def test_get_graphiql():
    elapsed = wait_until_open('localhost', 8080, 60)
    print("Waited", elapsed, "seconds for server to come up")
    response = requests.get('http://localhost:8080/static/graphiql')
    assert response.status_code == 200
