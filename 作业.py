# from selenium import webdriver    #qq空间登录
# from time  import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.maximize_window()
# dr.switch_to_frame('login_frame')
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('155554323')
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('shenme0.')
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.find_element_by_css_selector('#login_button').click()
# sleep(2)
# web = dr.find_element_by_xpath('/html/body/div[1]/div[11]/div[2]/iframe')
# dr.switch_to.frame(web)
# web = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ad = ActionChains(dr)
# ad.move_to_element(web)
# ad.drag_and_drop_by_offset(web,184,0)
# ad.perform()

# from selenium import webdriver    #商品加入购物车
# from time import sleep
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=69805951198_0_c03792dd513541e3aeb6a321d899fdad')
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('手机')
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
# sleep(3)
# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
# tt=dr.window_handles
# dr.switch_to_window(tt[-1])
# sleep(3)
# dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()



# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.maximize_window()
# class  quan():
#     dr = webdriver.Chrome()
#     dr.maximize_window()
#     def jiben(self):
#         # from selenium import webdriver
#         # from time import sleep
#         # dr=webdriver.Chrome()
#         # dr.maximize_window()
#         dr.get('https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=69805951198_0_c03792dd513541e3aeb6a321d899fdad')
#     def test_sou(self):
#         self.jiben()
#         dr.find_element_by_xpath('//*[@id="key"]').send_keys('手机')
#         dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()




import  requests      # 保存数据库
import  re
import pymysql
url='https://www.zhipin.com/c101010100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95'
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
res=requests.get(url=url,headers=head)
html=res.content.decode('utf-8')
patt=re.compile(r'ka="related-search-(.*?)">(.*?)</a>')
items=patt.findall(html)
print(items)
abc=pymysql.connect(host='192.168.0.38',port=3306,user='root',password='123456',charset='utf8')
a=abc.cursor()
a.execute('use xcz;')
# a.execute('create table bbq(序号 char(100),职位 char(100));')
for i,j in enumerate(items):
    a.execute('insert into bbq values("{}","{}");'.format(items[i][0],items[i][1]))

a.execute('select * from bbq;')
b=a.fetchall()
print(b)






# import HTMLTestRunnertest
# import unittest
# from selenium import webdriver    #商品加入购物车
# from time import sleep
# import time
# class zong(unittest.TestCase):
#     def test_1(self):
#         dr=webdriver.Chrome()
#         dr.maximize_window()
#         dr.get('https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=69805951198_0_c03792dd513541e3aeb6a321d899fdad')
#         dr.find_element_by_xpath('//*[@id="key"]').send_keys('手机')
#         dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
#         wd=dr.title
#         self.assertEqual(wd,'京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！')
#     def test_2(self):
#         dr = webdriver.Chrome()
#         dr.maximize_window()
#         dr.get('https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=69805951198_0_c03792dd513541e3aeb6a321d899fdad')
#         dr.find_element_by_xpath('//*[@id="key"]').send_keys('手机')
#         dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
#         sleep(3)
#         dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
#         tt=dr.window_handles
#         dr.switch_to_window(tt[-1])
#         sleep(3)
#         dr.find_element_by_xpath('//*[@id="InitCartUrl"]').click()
#         wd=dr.title
#         self.assertNotEqual(wd,'京东(JD.COM)')
# if __name__=='__main__':
#     suit=unittest.TestSuite()
#     suit.addTest(unittest.makeSuite(zong))
#     now=time.strftime('%Y Ym Yd %H-%M-%S',time.localtime(time.time()))
#     f=open('lian.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
#                                                      description='测试结果如下：',
#                                                      title='好分数测试报告',
#                                                      stream=f)
#     runner.run(suit)
#     f.close()





