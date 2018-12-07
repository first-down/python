# import requests
# import unittest
# import HTMLTestRunnertest
# import HTMLTestRunne
# import time
# import xlrd
# class xuexiao():
#     def tes_1(self,a):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring = {"filterInput": "{}".format(a)}
#         headers = {
#             'Content-Type': "application/x-www-form-urlencoded",
#             'cache-control': "no-cache,no-cache",
#             'cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#             'referer': "https://baijiahao.baidu.com/s?id=1601142086151469933&wfr=spider&for=pc",
#             'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
#             'x-devtools-emulate-network-conditions-client-id': "D804B14E-D1B4-4893-8ACF-5ABCB81C8702"}
#         response = requests.get(url=url, headers=headers, params=querystring)
#         html = response.json()
#         return html
#
# class 学校(unittest.TestCase,xuexiao):
#     # def setUp(self):  # 初始化测试环境 每次执行测试用例前执行
#     #     print(123)
#     # def tearDown(self):   #清理环境 每次用例执行之后执行
#     #     print(567)
#     def tes_数据(self):
#         shuju=[]
#         f=xlrd.open_workbook('test.xlsx')
#         sheet=f.sheets()[0]
#         num=sheet.nrows
#         for i in range(1,num):
#             aaa=sheet.row_values((i))
#             shuju.append(aaa)
#         return(shuju)
#     def test_1(self):
#         shuju=self.tes_数据()
#         html=self.tes_1(shuju[0][0])
#         self.assertEqual(html['code'],int(shuju[0][1]))
#         self.assertEqual(len(html['data']),702)   #判断这两个相等
#         self.assertEqual(html['data'][0]['schoolId1.5'], -1)
#     def test_2(self):
#         shuju=self.tes_数据()
#         html=self.tes_1(shuju[1][0])
#         self.assertNotEqual(html['code'],int(shuju[1][1]))      #判断这两个不相等
#
#     def test_3(self):
#         shuju=self.tes_数据()
#         html = self.tes_1(shuju[2][0])
#         self.assertEqual(html['code'],int(shuju[2][1]))
#
# if __name__=='__main__':
#     #生成测试报告   创建一个测试套件
#     suit=unittest.TestSuite()
#     #添加测试用例   将测试用例添加到测试套件中
#     suit.addTest(unittest.makeSuite(学校))    #将整个类中的所有测试添加到测试套件中
#     now=time.strftime('%Y Ym Yd %H-%M-%S',time.localtime(time.time()))
#     f=open('lian.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
#                                                  description='测试结果如下：',
#                                                  title='好分数测试报告',
#                                                  stream=f)
#     runner.run(suit)
#     f.close()
#     # suit.addTest(学校('test_1'))  添加这个类中对应的这个函数




