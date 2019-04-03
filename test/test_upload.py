import pytest
import dsim.upload
import pprint

@pytest.mark.skip
def test_upload():
    response = dsim.upload.upload('mydataset')
    assert response.status_code == 201
