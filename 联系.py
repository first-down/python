# from  selenium import webdriver
# from time  import sleep
# import time
# import unittest
# import HTMLTestRunnertest
# dr=webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[1]/div[1]/div[1]/a').click()
# sleep(3)
# wd = dr.window_handles
# dr.switch_to_window(wd[-1])
# dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div/span').click()
# sleep(3)
# dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').click()
# aa = dr.window_handles
# dr.switch_to_window(wd[-1])
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# wd = dr.find_element_by_tag_name('a').text
# print(wd)
#
# class  zongti(unittest.TestCase):
#     def test_1(self):
#         dr.maximize_window()
#         dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
#         a=dr.title
#         self.assertEqual(a,'摩尔精英招聘-专业的半导体招聘平台-半导体人才网-半导体工作')
#         sleep(5)
#     def test_2(self):
#         dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[1]/div[1]/div[1]/a').click()
#         sleep(3)
#         wd=dr.window_handles
#         dr.switch_to_window(wd[-1])
#         dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div/span').click()
#         sleep(3)
#         dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').click()
#         aa=dr.window_handles
#         dr.switch_to_window(wd[-1])
#         wd=dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').text
#         self.assertEqual(wd,'立即登录')
#
# if __name__=='__main__':
#     suit=unittest.TestSuite()
#     suit.addTest(unittest.makeSuite(zongti))
#     now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
#     f=open('adc.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
#                                                  description='测试结果如下：',
#                                                  title='web测试报告',
#                                                  stream=f)
#     runner.run(suit)
#     f.close()




import requests
import unittest
class jiben():
    def pac(self):
        url = "http://www.zhaoapi.cn/user/getUserInfo"
        querystring = {"uid": "1234"}
        headers = {'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "8c104254-6659-444b-b801-d38b5c53950e"}
        response = requests.request("POST", url, headers=headers, params=querystring)
        html=response.json()
        return html
    def oad(self):
        self.pac()
        pass
print(jiben().oad())
class shuju():
    def ss(self):
        with open('xxx.txt','r+',encoding='utf-8') as f:
            tt=f.readlines()
            return tt
    def tt(self):
        with open('a.txt','wd',encoding='utf-8') as f:
            f.readlines()