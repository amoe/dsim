import requests
import json
import sys

GRAPHQL_QUERY = """
    query retrieveData($personUri: String!) {
      dataSets {
        u33707283d426f900d4d33707283d426f900d4d0d__biaclusius {
          clusius_Persons(uri: $personUri) {
            tim_gender {
              value
            }
          }
        }
      }
    }
"""

# This comes from the metadata query
dataset_id = 'u33707283d426f900d4d33707283d426f900d4d0d__biaclusius'

qry_obj = {
    'query': GRAPHQL_QUERY, 
    'operationName': 'retrieveData',
    'variables': {
        'personUri': "http://timbuctoo.huygens.knaw.nl/datasets/clusius/Persons_PE00002125",
        'dataSet': dataset_id
    }
}

def do_query():
    response = requests.post(
        "http://localhost:8080/v5/graphql",
        json=qry_obj,
        headers={
            'authorization': 'null',   # You have to send the literal string 'null'
        }
    )
    content = response.json()
    return content

