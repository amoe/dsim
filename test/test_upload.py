import pytest
import dsim.upload
import pprint

def test_upload():
    response = dsim.upload.upload()
    pprint.pprint(response)
