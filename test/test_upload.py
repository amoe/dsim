import pytest
import dsim.upload
import pprint
import test_infrastructure.constants

def test_upload():
    response = dsim.upload.upload(test_infrastructure.constants.FIXTURE_DATASET_NAME)
    assert response.status_code == 201
