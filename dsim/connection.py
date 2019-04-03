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


if __name__ == '__main__':
    import sys
    wait_until_connected(sys.argv[1], int(sys.argv[2]))
