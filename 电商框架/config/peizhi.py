import requests
class beizhi():
    def jine_1(self,a,b):
        url='http://www.zhaoapi.cn/user/login'
        querystring = {"mobile": "{}", "password": "{}".format(a,b)}

        payload = ""
        headers = {'cache-control': "no-cache",'Postman-Token': "020c8252-f2a0-4a22-9910-3a8439984a5c"}
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        html=response.json()
        return html
    def jine(self,a):
        url = "http://www.zhaoapi.cn/user/getUserInfo"

        querystring = {"uid": "{}".format(a)}

        headers = {'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "2a1f16ec-27c2-4a04-b017-5de3e565aca1"}
        response = requests.request("POST", url, headers=headers, params=querystring)
        html=response.json()
        return html

