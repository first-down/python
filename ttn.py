# /usr/bin/env python
# -* encoding:utf-8 -*
# from selenium import webdriver
# from time  import sleep
# import re
# dr=webdriver.Chrome()
# dr.get('http://192.168.0.254')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# for i in range(1,5):
#     t=dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i)).get_attribute('src')
#     patt=re.compile('/imgs/(.*?).gif')
#     items=patt.findall(t)
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(items)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd=dr.switch_to_alert()   #切换到弹出框
# print(wd.text)
# wd.accept() #点击确定

# import xlrd
# ad=xlrd.open_workbook('rx.xls')
# sheet=ad.sheets()[0]
# a=sheet.nrows
# print(a)


# from selenium  import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('https://192.168.0.254:8889/')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# # 弹出框 (alert)
# sleep(2)
# wd=dr.switch_to_alert()   #切换到弹出框
# print(wd.text)
# wd.accept() #点击确定

# wd=dr.switch_to_alert()   #切换到弹出框
# wd.dismiss()      #点击取消
#wd.send_keys('内容')    #向弹出框输入内容


# from selenium  import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('http://www.alltuu.com/v')
# dr.maximize_window()
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('15836068251')
# sleep(2)
# wd=dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# sleep(2)
# for i in wd:
#     if '163.com' in  i.text:
#         i.click()

# from selenium import webdriver
# from time import sleep
# import re
# dr=webdriver.Chrome()
# dr.get('https://192.168.0.254:8889/')
# dr.maximize_window()
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# for i in range(1,5):
#     wd=dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i)).get_attribute('src')
#     patt=re.compile('/imgs/(.*?).gif')
#     items=patt.findall(wd)
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(items)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd=dr.switch_to_alert()
# wd.accept()
# sleep(3)
# dr.switch_to_frame('left')
# dr.find_element_by_xpath('//*[@id="04"]/span[2]').click()
# dr.find_element_by_xpath('//*[@id="041"]/span').click()
#
# dr.switch_to_default_content()
# dr.switch_to_frame('mainFrame')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()

#移动滚动条  属于浏览器的  javascript语言
# dr.get('http://www.alltuu.com/v')
# dr.maximize_window()
#1根据页面的高度来移动滚动条
#控制滚动条的javascript的代码
# js='var q=document.documentElement.scrollTop=10000'    #一万表示所有页面的高度    数字越大滚动条越往下
# dr.execute_script(js)   #执行javaScript 语句

#2.根据定位定位到的元素来移动滚动条
#定位一个元素
# target=dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[3]/div/div[1]/p[1]')
# js="arguments[0].scrollIntoView();"
# dr.execute_script(js,target)



# from  selenium.webdriver.common.action_chains import ActionChains
# dr.get('https://i.qq.com/')
# dr.maximize_window()
# dr.switch_to_frame('login_frame')
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(1583606821)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('asdas')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# # while True:
# wt=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(wt)
# sleep(2)
# while True:
#     s=150
#     target=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
#     sleep(1)
#     ActionChains(dr).drag_and_drop_by_offset(target,s,0).perform() #滑动窗口
#     s+=2

import  selenium.webdriver.support.ui  as  ui
from   selenium  import webdriver
from  time  import sleep
dr=webdriver.Chrome()
dr.get('http://www.moore.ren/')
dr.maximize_window()
sleep(2)
#强制等待   sleep（2）
#职能等待     设置控制器dr等待
# until=ui.WebDriverWait(dr,10)
# until.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())



# #  is_displayed()  判断元素是否显示     这个两个结果  可以用作if 判断  结果： trie  fiase
# #  is_enabled()  判断元素是否为灰化状态     如果同意协议没有点击   就是灰化状态
# un=dr.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[11]/div[2]').is_displayed()
# print(un)



#截图
# dr.get_screenshot_as_file(r'C:\Users\幸存者\Desktop\大侄子\a.png')
# dr.quit()



# dr.get_screenshot_as_png()
# dr.save_screenshot('aaa.png')