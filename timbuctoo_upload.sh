timbuctoo_base=/home/amoe/download/timbuctoo-6.16
data_path=timbuctoo-instancev4/src/test/resources/nl/knaw/huygens/timbuctoo/v5/bia_clusius.ttl
complete_path="${timbuctoo_base}/${data_path}"
filetype="text/turtle"

curl -v -F "file=@${complete_path};type=${filetype}" -F "encoding=UTF-8" -H "Authorization: fake" 'http://localhost:8080/v5/u33707283d426f900d4d33707283d426f900d4d0d/mydataset/upload/rdf?forceCreation=true'
