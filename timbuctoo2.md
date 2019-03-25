query queryName($dataSet:ID!){
    field(arg: "value") {
             subField{value}
    }
}

timbuctoo uses the following conf to store sets

    volumes:
      - ./timbuctoo-data/:/mapped-data

this is meaning that the subdirectory `timbuctoo-data` gets mapped locally ;
this is local data set storage that won't be removed 


