import pytest

def test_get_graphiql():
    response = requests.get('http://localhost:8080/static/graphiql')
    assert response.status_code == 200
