import requests
import SearchYT as Yt
import time
inicio = time.time()


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
Title = data['response']['docs'][i]['title'] + ' - ' + data['response']['docs'][i]['band']
print(Title)
Yt.argparser.add_argument("--q", help="Search term", default="Instumental "+ Title)
Yt.argparser.add_argument("--max-results", help="Max results", default=5)
args = Yt.argparser.parse_args()

try:
    import threading
    t = threading.Thread(target=Yt.youtube_search, args=(args,))
    t.start()

except Yt.a.errors.HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

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

fim = time.time()
print(fim - inicio)
