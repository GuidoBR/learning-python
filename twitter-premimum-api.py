import requests
import json
import csv
import time


headers = {
    'authorization': 'Bearer ',
    'content-type': 'application/json'
}
# "query":"retweets_of:EditoraSuma",

request_params = {
    'query': 'url:1380581459476541448',
    'maxResults': '100',
    'fromDate':'202104090000',
    'toDate':'202105010000'
}

url = "https://api.twitter.com/1.1/tweets/search/30day/dev.json"


print("Começando requisições para API do Twitter")
hasNext = True
tweets_data = []

r = requests.post(url, data=json.dumps(request_params), headers=headers)
req_count = 1
while hasNext:
    print('Requisição {}'.format(req_count))
    if r.status_code != 200:
        print("Erro na requisição: ", r.status_code)
        print("Erro na requisição: ", r.text)
        break

    data = r.json()
    for tweet in data.get('results'):
         tweets_data.append(tweet.get('id'))

    if len(tweets_data) >= 3000:
        print('Tweets recuperados: {}'.format(len(tweets_data)))
        print('Escrevendo na planilha.csv...')
        with open('planilha.csv', mode='a') as planilha:
            writer = csv.writer(planilha, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for tweet in tweets_data:
                writer.writerow([tweet])
        tweets_data = []
        print('Pausa pro café... Twitter limita a quantidade de requisições que posso a cada 15min...')
        time.sleep(901)

    hasNext = True if data.get('next') else False
    if hasNext:
        req_count += 1 
        request_params['next'] = data.get('next')
        print('Fazendo próxima requisição ... {}'.format(data.get('next')))
        r = requests.post(url, data=json.dumps(request_params), headers=headers)




