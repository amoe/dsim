import requests
import json
import sys

GRAPHQL_QUERY = """
query CollectionMetadata {
  dataSets {
    u33707283d426f900d4d33707283d426f900d4d0d__mydataset {
      metadata {
        collectionList {
          items {
            collectionId
            uri
          }
        }
      }
    }
  }
}
"""

# This comes from the metadata query
dataset_id = 'u33707283d426f900d4d33707283d426f900d4d0d__mydataset'

qry_obj = {
    'query': GRAPHQL_QUERY, 
    'operationName': 'CollectionMetadata',
    'variables': {}
}


response = requests.post(
    "http://localhost:8080/v5/graphql",
    json=qry_obj,
    headers={
        'authorization': 'null',   # You have to send the literal string 'null'
    }
)

content = response.json()
json.dump(content, sys.stdout, indent=4)
print()



