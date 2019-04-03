import pytest
import pprint
import dsim.query
import test_infrastructure.constants



EXPECTED_RESULT = {
    'data': {
        'dataSets': {
            'u33707283d426f900d4d33707283d426f900d4d0d__testdataset': {
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
    result = dsim.query.do_query(previously_uploaded_dataset)
    assert result == EXPECTED_RESULT
