#! /bin/sh

curl -v -F "file=@/home/amoe/bia_clusius.ttl;type=text/turtle" -F "encoding=UTF-8" -H "Authorization: fake" http://localhost:8080/v5/u33707283d426f900d4d33707283d426f900d4d0d/mydataset/upload/rdf?forceCreation=true



