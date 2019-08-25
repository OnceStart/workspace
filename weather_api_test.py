import requests
from urllib import parse

data = {'city' : r'北京'}
city = parse.urlencode(data).encode('utf-8')
url = 'http://t.weather.sojson.com/api/weather/city/101030100'

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
r = requests.get(url, headers = header)
response_data = r.json()
print(response_data['data']['forecast'][0]['low'])
