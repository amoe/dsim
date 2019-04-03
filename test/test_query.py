import pytest
import pprint
import dsim.query

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

# XXX: This won't work because it relies on existing state.
def test_query(previously_uploaded_dataset):
    result = dsim.query.do_query('foo')
    assert result == EXPECTED_RESULT
