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

