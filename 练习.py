# /usr/bin/env python
# -*- conding:utf
import requests
import unittest
import HTMLTestRunnertest
import HTMLTestRunne
import time
import xlrd
import xlwt
import pymysql

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
class date(unittest.TestCase,学校_查询):
    def duqu(self):
        t=[]
        x=xlrd.open_workbook('test.xlsx')
        sheet=x.sheets()[0]
        a=sheet.nrows
        for  i in range(1,a):
            t.append(sheet.row_values((i)))
        return(t)
    def test_1(self):
        c=self.duqu()
        html=self.学校_快查(c[0][0])
        self.assertEqual(html['code'], int(c[0][1]))
    def test_2(self):
        c=self.duqu()
        html=self.学校_快查(c[1][0])
        self.assertTrue(html)
    def test_3(self):
        c=self.duqu()
        html=self.学校_快查(c[2][0])
        self.assertIn(html['data'],'北京')
# if __name__ in '__main__':
#     unittest.main()





import requests
import unittest
import HTMLTestRunnertest
import time
import re




