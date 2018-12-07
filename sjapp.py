# from appium import webdriver
# import time
# desired_caps={ 'platformName':'Android',   #版本
#                  #'platformVersion':'6.0.1',  #banben
#               'deviceName':'127.0.0.1:62001',  #设备名
#               'appPackage':'sogou.mobile.explorer',   #安装名
#               'appActivity':'BrowserActivity'}   #activity的值
# print(3)
# driver =  webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# print(123)
#
#
# driver.find_element_by_id('sogou.mobile.explorer:id/vs').click()
# print(1234)
# time.sleep(3)



# from appium import webdriver
# import time
#
# desired_caps = {'platformName': 'Android',
#                 # 'platformVersion':'6.0',
#                 'deviceName':'127.0.0.1:62001',
#                 'appPackage':'com.netease.cloudmusic',
#                 'appActivity':'activity.LoadingActivity'}
# print(2314)
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# # time.sleep(20)
#
# print("立即体验")
# driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
# time.sleep(3)
# #
# print("点击抽屉菜单")
# driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
# time.sleep(3)
#
# print("立即登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
# time.sleep(3)
#
# print("手机号登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
# time.sleep(3)
#
# print("输入手机号")
# driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
# time.sleep(3)
#
# print("输入密码")
# driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("gao19930903")
# time.sleep(3)
#
# print("登录")
# driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
# time.sleep(3)
#
# #断言
# print("点击抽屉菜单")
# driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
# time.sleep(3)
#
#
# print("用户名")
# title=driver.find_element_by_id("com.netease.cloudmusic:id/ac2").text
# aa= "用户507297819"
# if title==aa:
#     print("登录成功")
# #
# driver.quit()





# from appium import webdriver
# import time,unittest
#
# class Login(unittest.TestCase):
#     def setUp(self):
#         desired_caps = {'platformName': 'Android',
#    #                'platformVersion':'6.0',
#                     'deviceName': '127.0.0.1:62001',
#                     'appPackage': 'com.netease.cloudmusic',
#                     'appActivity': 'activity.LoadingActivity'}
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         time.sleep(20)
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_login(self):
#
#         print("立即体验")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
#         time.sleep(6)
#
#         print("点击抽屉菜单")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
#         time.sleep(5)
#
#         print("立即登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
#         time.sleep(3)
#
#         print("手机号登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
#         time.sleep(3)
#
#         print("输入手机号")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
#         time.sleep(3)
#
#         print("输入密码")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("gao19930903")
#         time.sleep(3)
#
#         print("登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
#         time.sleep(3)
#
#         # 断言
#         print("点击抽屉菜单")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
#         time.sleep(2)
#         title = self.driver.find_element_by_id("com.netease.cloudmusic:id/ac2")
#         self.assertEqual(title.text, "用户507297819")
#         print("登陆成功")
#
#     def test_login2(self):
#         print("执行第二条测试")
#         print("立即体验")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
#         time.sleep(6)
#
#         print("点击抽屉菜单")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
#         time.sleep(5)
#
#         print("立即登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
#         time.sleep(3)
#
#         print("手机号登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
#         time.sleep(3)
#
#         print("输入手机号")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
#         time.sleep(3)
#
#         print("输入密码")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("19930903")
#         time.sleep(3)
#
#         print("登录")
#         self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
#         time.sleep(5)
#
#         title = self.driver.find_element_by_id('com.netease.cloudmusic:id/pt')
#         self.assertEqual(title.text, "登录")
#         print("登陆失败")
#
# if __name__ == '__main__':
#     unittest.main()



import os
os.rename('1111.py','sjapp.py')