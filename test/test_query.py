import pytest
import pprint
import dsim.query_clusius

# def test_query_dataset(previously_uploaded_dataset):
#     pprint.pprint(previously_uploaded_dataset)
#     assert True


EXPECTED_RESULT = {
    'data': {
        'dataSets': {
            'u33707283d426f900d4d33707283d426f900d4d0d__biaclusius': {
                'clusius_Persons': {
                    'tim_gender': {
                        'value': 'MALE'
                    }
                }
            }
        }
    }
}

@pytest.mark.skip
def test_query():
    result = dsim.query_clusius.do_query()
    assert result == EXPECTED_RESULT
