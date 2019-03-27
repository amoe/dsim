import requests
import json
import sys


# See https://graphql.org/learn/serving-over-http/

GRAPHQL_QUERY = """
query Home {                                
  promotedDataSets {
    imageUrl {
      value
      __typename
    }
    title {
      value
      __typename
    }
    description {
      value
      __typename
    }
    dataSetId
    __typename
  }
  allDataSets {
    title {
      value
      __typename
    }
    description {
      value
      __typename
    }
    dataSetId
    dataSetName
    __typename
  }
  aboutMe {
    id
    name
    personalInfo
    __typename
  }
}
"""

qry_obj = {
    'query': GRAPHQL_QUERY, 
    'operationName': 'Home',
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
