
import requests
import json

url1 = 'https://safebrowsing.urlsec.qq.com/v4/threatListUpdates:fetch'

data1 = {
'key':'x3dFV-lKdZ-HyfqFgedjQAIzaSyBbT4JTuz7jdG'
}


def send_get(url, data):
	res = requests.get(url=url,data=data).json()
	return json.dumps(res,indent=2,sort_keys=True)


print(send_get(url1, data1))