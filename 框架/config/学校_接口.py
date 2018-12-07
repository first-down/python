#/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
class 学校_查询():
    def 学校_快查(self,a):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring = {"filterInput": "{}".format(a)}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache,no-cache",
            'cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
            'referer': "https://baijiahao.baidu.com/s?id=1601142086151469933&wfr=spider&for=pc",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
            'x-devtools-emulate-network-conditions-client-id': "D804B14E-D1B4-4893-8ACF-5ABCB81C8702"}
        response = requests.get(url=url, headers=headers, params=querystring)
        html = response.json()
        return html
    def 学校_考试快查(self,a):
        pass
    def 学校_列表(self):
        pass