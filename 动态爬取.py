import requests
import re
import xlwt
class zhilian():
    def qinqiu(self):
        a=['https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.01097835&x-zp-page-request-id=e0f56c50c62c4f84b5bfaec445247355-1541768917339-961731'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.27393779&x-zp-page-request-id=7161854b4ce84b72a606216d33ca1a46-1541814546568-870708'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.34573786&x-zp-page-request-id=5ca57d70af1245d688194da90a1acf7f-1541814748861-951786'
                   ,'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=763&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.93934657&x-zp-page-request-id=da763ba5f7124d928d0c5be0471767b9-1541814818979-678695']
        aa=[]
        for i in a:
            for j in range(0,180,60):
                kk=i.format(j)
                aa.append(kk)

        zhiwei1=[]
        xinzi1=[]
        didian1=[]
        time1=[]
        renshu1=[]
        jinyan1=[]
        for dd in aa:
            url=dd
            head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
            response=requests.get(url=url,headers=head)
            html=response.content.decode('utf-8')
            zhiwei=re.compile(r'jobName":"(.*?)","',re.S)
            xinzi=re.compile(r'"salary":"(.*?)","',re.S)
            didian=re.compile(r'city":{"items":(.*?)"},"applyType',re.S)
            time=re.compile(r'updateDate":"(.*?)","',re.S)
            renshu=re.compile(r'size":{"(.*?)"},"type',re.S)
            jinyan=re.compile(r'workingExp":{"(.*?)"},"eduLevel')

            items=zhiwei.findall(html)
            zhiwei1.append(items)
            items1=xinzi.findall(html)
            xinzi1.append(items1)
            items2=time.findall(html)
            time1.append(items2)
            items3=renshu.findall(html)
            renshu1.append(items3)
            items4=didian.findall(html)
            didian1.append(items4)
            items5=jinyan.findall(html)
            jinyan1.append(items5)
        return   zhiwei1,xinzi1,didian1,time1,renshu1,jinyan1

    def baocun(self,a,b,c,d,e,nn):
        dd=1
        f=xlwt.Workbook(encoding='utf-8')
        sheet = f.add_sheet('智联')
        sheet.write(0,0,'职位')
        sheet.write(0,1,'薪资')
        sheet.write(0,2,'公布时间')
        sheet.write(0,3,'公司人数')
        sheet.write(0,4,'公司地址')
        sheet.write(0,5,'工作经验')
        k = 1
        m = 1
        n = 1
        aa = 1
        bb = 1
        cc = 1
        for j in range(12):
            for i in a[j]:
                sheet.write(k, 0, '{}'.format(i))
                k += 1
        for j in range(12):
            for i in b[j]:
                sheet.write(m, 1, '{}'.format(i))
                m += 1
        for j in range(12):
            for i in c[j]:
                sheet.write(n, 2, '{}'.format(i))
                n += 1
        for j in range(12):
            for i in d[j]:
                i = i.split('"')
                sheet.write(aa, 3, '{}'.format(i[-1]))
                aa += 1
        for j in range(12):
            for t in e[j]:
                t = t.split('"')
                sheet.write(bb, 4, '{}'.format(t[-1]))
                bb += 1
        for j in range(12):
            for ff in nn[j]:
                ff = ff.split('"')
                sheet.write(cc, 5, '{}'.format(ff[-1]))
                cc += 1

        f.save('智联招聘.xls')

# aa=zhilian()
# a,b,c,d,e,nn=aa.qinqiu()
# aa.baocun(a,b,c,d,e,nn)
from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time   import sleep

# de=webdriver.Chrome()
# de.get('http://www.moore.ren/')
# #  link_text 通过文本定位   保证定位元素的唯一性   只能定位屏幕上显示的
# de.maximize_window()
# de.find_element_by_link_text('登录').click()
# de.find_element_by_partial_link_text('登').click()    #通过模糊文本来定位

# de.find_element_by_tag_name('').click()  #通过标签的名称来等位  通常用于多个元素的定位

#通过xpath路径定位    xpath ：路径标记语言    绝对路径（/）  相对路径（//）   xml：可扩展标记语言

# de.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()

#通过css定位
# de.find_element_by_css_selector('#user-nomal > div.login-wrap > div.before-login > li.no-login > a').click()

# 1.id( )  2.name 3.class 4.tegname  5.link_text  6.partial_link_text   7.xpath  8.css


# wd=de.find_elements_by_class_name('menu-box')   #定位多个class属性的值为 menu——box的元素     数据类型是列表
# for i in wd:
#     ActionChains(de).move_to_element(i).perform()
#     sleep(2)
# de.quit()


# wd=de.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')     # 层级定位
# for i in wd:
#     ActionChains(de).move_to_element(i).perform()

# wd=de.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# print(wd.get_attribute('href'))   #获取元素的某一个属性对应的值
#
#
# wd=de.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)   #获取这个标签的文本信息




# dr=webdriver.Chrome()
# dr.get('https://192.168.0.254:8889')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# for i in range(1,5):
#     wd=dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i)).get_attribute('src')
#     patt=re.compile('/imgs/(.*?).gif')
#     t=patt.findall(wd)
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(t)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()

dr=webdriver.Chrome()     #携程
dr.get('http://www.ctrip.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=baidu81&campaign=CHNbaidu81&adid=index&gclid=&isctrip=T')
dr.maximize_window()
dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
s=['x','x','阿','焦','你','是','最','胖','的','加','油']
for i in range(2,11):
    wd=dr.find_element_by_xpath('//*[@id="J_roomCountList"]/option[{}]'.format(i)).click()
    dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
    dr.find_element_by_xpath('//*[@id="HD_TxtKeyword"]').send_keys(s[i])
dr.find_element_by_xpath('//*[@id="HD_CityName"]').send_keys('杭州')
dr.find_element_by_xpath('/html/body/div[5]').click()
dr.find_element_by_xpath('//*[@id="HD_Btn"]').click()

# #
# dr=webdriver.Chrome()
# # dr.get('http://www.moore.ren/')
# # dr.maximize_window()
# # sleep(2)
# # dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# # print(dr.current_window_handle)  #获取当前窗口的句柄   句柄是窗口
# # wd=dr.window_handles   # 获取所用窗口的句柄
# # dr.switch_to_window(wd[-1])   #根据句柄切换窗口
# # print(dr.title)   #获取当前窗口的title
#
#
#
#
# #框架是镶嵌在web上的一个窗口
# dr.get('https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F947361061&rd=1')
#
# dr.switch_to_frame('login_frame')  #切换到内嵌框架中 ，只能根据：id，name，定位到框架，属性的值来切换
#
# #定位到框架来切换框架
# # dw=dr.find_element_by_xpath('//*[@id="login_frame"]')
# # dr.switch_to_frame(dw)
#
#
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(947361061)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('shenme0.')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
#
#
# dr.switch_to.default_content() # 退出到原始的页面
# dr.find_element_by_xpath('//*[@id="lay"]/div[2]/div[1]/div[1]/ul/li[1]/a/i').click()

# dr.switch_to.parent_frame('//*[@id="lay"]/div[2]/div[1]/div[1]/ul/li[1]/a/i')    根据上一层的框架id name 定位框架来切换到上一层框架