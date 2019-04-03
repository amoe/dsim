import pytest
import dsim.upload

FIXTURE_DATASET_NAME = 'foo'

@pytest.fixture
def previously_uploaded_dataset():
    response = dsim.upload.upload(FIXTURE_DATASET_NAME)
    return FIXTURE_DATASET_NAME
