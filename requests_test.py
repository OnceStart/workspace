import requests
import json
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

base_url = 'http://httpbin.org'

# r = requests.get(base_url + '/get')
# print(r.status_code)

# r = requests.post(base_url + '/post')
# print(r.status_code)

# r = requests.put(base_url + '/put')
# print(r.status_code)

# r = requests.delete(base_url + '/delete')
# print(r.status_code)

# param_data = {'user':'dustin', 'passwd':'666'}
# r = requests.get(base_url + '/get', params = param_data)
# print(r.url)
# print(r.status_code)

# form_data = {'user':'dustin', 'passwd':'777'}
# r = requests.post(base_url + '/post', data = form_data)
# print(r.headers)
# print(r.status_code)
# print(r.json())

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
# r = requests.get('https://www.zhihu.com/explore', headers = header)
# print(r.text)

# cookie = {'user':'dustin'}
# r = requests.get(base_url + '/cookies', cookies = cookie)
# print(r.cookies)
# for key,value in r.cookies.items():
# 	print(key + ' : ' + value)

# r = requests.get('https://www.baidu.com')
# print(r.headers)

# session = requests.session()
# session.get("https://www.baidu.com")
# set_cookie = requests.utils.dict_from_cookiejar(session.cookies)
# print(set_cookie)

# file = {'file' : open('aaa.png', 'rb')}
# r = requests.post(base_url + '/post', files = file)
# print(r.text)

# s = requests.session()
# r = s.get('https://www.baidu.com')
# print(r.cookies)

# r = s.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
# 	print(key + ' : ' + value)

# r = requests.get(base_url + '/basic-auth/dustin/123', auth = HTTPBasicAuth('dustin', '123'))
# print(r.text)
# r = requests.get(base_url + '/digest-auth/auth/dustin/567', auth = HTTPDigestAuth('dustin', '567'))
# print(type(r.text))


r = requests.get(base_url + '/stream/10')
print(r.status_code)
if r.encoding is None:
	r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode = True):
	if line:
		data = json.loads(line)
		print(type(data))