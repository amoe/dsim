#! /bin/sh


curl 'http://localhost:8080/v5/graphql' -H 'Origin: http://localhost:3006' \
  -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'authorization: null' -H 'content-type: application/json' -H 'accept: application/json' -H 'Referer: http://localhost:3006/' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.122 Safari/537.36' -H 'Connection: keep-alive' -H 'DNT: 1' --data-binary '{"operationName":"Home","variables":{},"query":"query Home {\n  promotedDataSets {\n    imageUrl {\n      value\n      __typename\n    }\n    title {\n      value\n      __typename\n    }\n    description {\n      value\n      __typename\n    }\n    dataSetId\n    __typename\n  }\n  allDataSets {\n    title {\n      value\n      __typename\n    }\n    description {\n      value\n      __typename\n    }\n    dataSetId\n    dataSetName\n    __typename\n  }\n  aboutMe {\n    id\n    name\n    personalInfo\n    __typename\n  }\n}\n"}' --compressed
