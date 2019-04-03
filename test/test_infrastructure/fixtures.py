import pytest
import dsim.upload
import test_infrastructure.constants

@pytest.fixture
def previously_uploaded_dataset():
    dataset_name = test_infrastructure.constants.FIXTURE_DATASET_NAME
    response = dsim.upload.upload(dataset_name)
    return dataset_name
