import requests


url = "http://www.boardgamegeek.com/xmlapi/boardgame/86174"

headers = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "82b1a82c-7758-40d7-a5ad-03d11703bbef,8fc8e64b-dbf7-4d12-b50b-9657df004de7",
    'Host': "www.boardgamegeek.com",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "http://www.boardgamegeek.com/xmlapi/boardgame/86174",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)
