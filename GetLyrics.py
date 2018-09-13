import requests

url = "https://api.vagalume.com.br/search.artmus"

querystring = {"apikey":"deef00ef0eb28795b026393460b7fd4c","q":"Rap Lord","limit":"5"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "872a0fd4-f82c-44fb-8e59-3ce88c7e12a1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

import json

data = json.loads(response.text)

for i in range(len(data['response']['docs'])):
    try:
        print("Musica " +str(i+1) + ': ' + data['response']['docs'][i]['title'] + ' - ' + data['response']['docs'][i]['band'])
        print()
    except Exception:
        pass

i = int(input("Selecione a música para ver a letra: "))-1
print(data['response']['docs'][i]['title'] + ' - ' + data['response']['docs'][i]['band'])
id = data['response']['docs'][i]['id']

url = "https://api.vagalume.com.br/search.php"

querystring = {"apikey":"deef00ef0eb28795b026393460b7fd4c","musid":id}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "0808e6a7-132e-49a2-858f-13dbe59c5b24"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
print(data["mus"][0]['text'])