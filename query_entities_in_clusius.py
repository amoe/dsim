import requests
import json
import sys

GRAPHQL_QUERY = """
query retrieveData {
  dataSets {
    u33707283d426f900d4d33707283d426f900d4d0d__biaclusius {
      clusius_Persons(uri:"PE00011637") {
        tim_birthDate
      }
    }
  }
}
"""

# This comes from the metadata query
dataset_id = 'u33707283d426f900d4d33707283d426f900d4d0d__mydataset'

qry_obj = {
    'query': GRAPHQL_QUERY, 
    'operationName': 'retrieveData',
    'variables': {
#        'dataSet': dataset_id
    }
}

print(qry_obj)


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


2http://timbuctoo.huygens.knaw.nl/datasets/clusius/Persons_PE00002125"


query retrieveData {
  dataSets {
    u33707283d426f900d4d33707283d426f900d4d0d__biaclusius {
      clusius_Persons(uri: "http://timbuctoo.huygens.knaw.nl/datasets/clusius/Persons_PE00002125") {
				tim_gender {
          value
        }
      }
    }
  }
}


And also

query retrieveData {
  dataSets {
    u33707283d426f900d4d33707283d426f900d4d0d__biaclusius {
      clusius_PersonsList {
				items {
          uri
        }
      }
    }
  }
}
