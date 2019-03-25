import requests

endpoint_parameters = {
    'user_id': 'u33707283d426f900d4d33707283d426f900d4d0d',
    'dataset_name': 'mydataset'
}

endpoint_template = 'http://localhost:8080/v5/{user_id}/{dataset_name}/upload/rdf?forceCreation=true'
real_endpoint = endpoint_template.format_map(endpoint_parameters)

headers = {
    'Authorization': 'fake',
}

# This is crucial and defined in the following class,
# nl.knaw.huygens.timbuctoo.v5.dropwizard.endpoints.RdfUpload
UPLOAD_DATA_FORM_PARAMETER = 'file'

path = 'foafsample.ttl'
with open(path, 'rb') as f:
    file_tuple = (path, f, 'text/turtle')

    files = {UPLOAD_DATA_FORM_PARAMETER: file_tuple}

    payload = {'encoding': 'UTF-8'}
    response = requests.post(real_endpoint, headers=headers, data=payload, files=files)
    print(dir(response))
