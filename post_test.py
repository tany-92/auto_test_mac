import requests
import json

url1 = 'https://t-auth3.fvt.tujia.com/ios/api/condition/list.api'

data1 = {
	"hotelId": 189,
	"date": "2020-03-25",
	"pageSize": 30,
	"pageNum": 1
}


def send_post(url, data):
    res = requests.post(url=url, data=data)
    return res.json()


print(send_post(url1, data1))