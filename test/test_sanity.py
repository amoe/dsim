import pytest
import dsim.query_clusius
import pprint

def test_sanity():
    assert 2 + 2 == 4

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

def test_query():
    result = dsim.query_clusius.do_query()
    assert result == EXPECTED_RESULT
