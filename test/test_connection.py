import pytest
import socket
import requests
import time

def http_connection_works(url):
    try:
        requests.get(url)
        return True
    except requests.exceptions.ConnectionError as e:
        return False

def wait_until_connected(url, timeout):
    elapsed = 0
    while not http_connection_works(url):
        time.sleep(1)
        elapsed += 1
        if elapsed > timeout:
            raise Exception('timed out waiting for server to come up')
    return elapsed

def test_get_graphiql():
    elapsed = wait_until_connected('http://localhost:8080/static/graphiql', 60)
    print("Waited", elapsed, "seconds for server to come up")
    response = requests.get('http://localhost:8080/static/graphiql')
    assert response.status_code == 200
