# -*-coding:utf-8-*-
#接口测试： 发送请求，来验证响应是否符合需求的过程
# postman\jmeter
#requests 发送http请求  assert 这个函数来做断言处理
import requests
import unittest   #python自带单元测试自动化框架        #封装了检验返回结果的方法
# unittest.testCase   : 用来做来用例管理
# unittest.testSuit    ：测试套件，多个测试用例集合在一起
# unittest.testLoader  :将测试用例加载到测试套件中
#enittest.testRunner    : 执行测试用例



def tes_学校(a):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos'
        #a=input('>>>')
        querystring={"filterInput":"{}".format(a)}
        headers={
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache,no-cache",
        'cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
        'referer': "https://baijiahao.baidu.com/s?id=1601142086151469933&wfr=spider&for=pc",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36",
        'x-devtools-emulate-network-conditions-client-id': "D804B14E-D1B4-4893-8ACF-5ABCB81C8702"}
        response=requests.get(url=url,headers=headers,params=querystring)
        aaa=response.json()
        return aaa






#assert html ['code']==0    进行断言




# unittest.testCase   : 用来做来用例管理
# unittest.testSuit    ：测试套件，多个测试用例集合在一起
# unittest.testLoader  :将测试用例加载到测试套件中
#enittest.testRunner    : 执行测试用例



# class 学校(unittest.TestCase):
#     def setUp(self):  # 初始化测试环境 每次执行测试用例前执行
#         print(123)
#     def tearDown(self):   #清理环境 每次用例执行之后执行
#         print(567)
#     def test_1(self):
#         html=tes_学校('北京')
#         self.assertEqual(html['code'], 0)
#         self.assertEqual(html['data'][0]['schoolName'],'北京七中')   #判断这两个相等
#     def test_2(self):
#         html=tes_学校('adcd')
#         self.assertNotEqual(html['code'],0)      #判断这两个不相等
# if __name__=='__main__':
#     unittest.main()



import requests
import unittest
import HTMLTestRunnertest
import HTMLTestRunne
import time
import xlrd
class xuexiao():
    def tes_1(self,a):
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

class 学校(unittest.TestCase,xuexiao):
    # def setUp(self):  # 初始化测试环境 每次执行测试用例前执行
    #     print(123)
    # def tearDown(self):   #清理环境 每次用例执行之后执行
    #     print(567)
    def tes_数据(self):
        shuju=[]
        f=xlrd.open_workbook('test.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(1,num):
            aaa=sheet.row_values((i))
            shuju.append(aaa)
        return(shuju)
    def test_1(self):
        shuju=self.tes_数据()
        html=self.tes_1(shuju[0][0])
        self.assertEqual(html['code'],int(shuju[0][1]))
        self.assertEqual(html['data'][0]['schoolName'],shuju[0][2])   #判断这两个相等
        self.assertEqual(html['data'][0]['schoolId1.5'], -1)
    def test_2(self):
        shuju=self.tes_数据()
        html=self.tes_1(shuju[1][0])
        self.assertNotEqual(html['code'],int(shuju[1][1]))      #判断这两个不相等

    def test_3(self):
        shuju=self.tes_数据()
        html = self.tes_1(shuju[2][0])    #调用数据的这个函数
        self.assertEqual(html['code'],int(shuju[2][1]))
if __name__=='__main__':
    #生成测试报告   创建一个测试套件
    suit=unittest.TestSuite()
    #添加测试用例   将测试用例添加到测试套件中
    suit.addTest(unittest.makeSuite(学校))    #将整个类中的所有测试添加到测试套件中
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    f=open('adc.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
                                                 description='测试结果如下：',
                                                 title='好分数测试报告',
                                                 stream=f)
    runner.run(suit)
    f.close()
    # suit.addTest(学校('test_1'))  添加这个类中对应的这个   函数






    # unittest.main()

