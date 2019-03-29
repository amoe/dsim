# dsim

So it's clear that we use `operationName` to define which operation to invoke.
This refers to a defined query.  You get 500 if undefined.

timbuctoo_1      | graphql.execution.UnknownOperationException: Unknown operation named 'Home0'.

So if you go like this:

    query retrieveData($dataSet:ID!){
      dataSet(dataSetId:$dataSet){
        <collection>{
            <items>{
                <property1>
                <property2>
                ...
            }
        }
      }
    }

The thing acts as like a function call.  So 'variables' defined formal
parameters.

Clearly collection is 



The collection, items, etc are all features of the dataset.

Once you upload the properly formatted RDF you get stuff like this.


            {
                "__typename": "DataSetMetadata",
                "dataSetId": "u33707283d426f900d4d33707283d426f900d4d0d__biaclusius",
                "description": {
                    "__typename": "u33707283d426f900d4d33707283d426f900d4d0d__biaclusius_value_xsd_string",
                    "value": "Biographical data of the Digital Web Centre for the History of Science (DWC)"
                },
                "dataSetName": "biaclusius",
                "title": {
                    "__typename": "u33707283d426f900d4d33707283d426f900d4d0d__biaclusius_value_xsd_string",
                    "value": "DWC Data"
                }
            }



For the format of graphql queries try this.

https://graphql.org/learn/serving-over-http/

Graphql queries are constructed through graphql-java

SubSel

This error

`SubSelectionRequired` means that you tried to return a non-scalar directly.
Index into it instead.  In timbuctoo the key insight is that every property has both `value` and `type` sub fields.

HTTP/2 can confront graphql by removing multi request overhead




"http://timbuctoo.huygens.knaw.nl/datasets/clusius/Persons_PE00002125"


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

