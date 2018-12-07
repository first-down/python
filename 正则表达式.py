#导入正则的模块   re   #正则表达式只能匹配字符串
import re
#贪婪模式：尽可能多的去匹配最后的字符串   #带有？的是非贪婪，带有*的贪婪模式
# 非贪婪模式：尽可能少的去匹配最后的字符串
a="""qwe12312
qwe3123123qwe"""

#将要匹配的正则编译      *匹配前一个字符一次或者多次   点.匹配任意一个字符   除了换行符
b=re.compile('qwe(.*?)QWE',re.S.I)   #在编译的后面加上，re.S  让点可以匹配包括换行符在内的所有字符
#到目的字符串中去查找                #re。I匹配的字符不区分大小写
c=b.findall(a)
print(c)




#爬虫的第一步
import re
import requests
class Qiushi(object):
    def qingshi(self,page):
        url='https://www.qiushibaike.com/text/page/{}/'.format(page)
        #发送请求
        a=requests.get(url=url)
        #读取的方式：1，以字符串的方式读取  2，以字节码的方式读取
        html=a.content.decode('utf-8')#字节码的方式获取
        return html
# 第二步：分析html文件，过滤并下载想要的资源
    def guolv(self,adc):
        patt=re.compile('<div class="content">(.*?)</div>',re.S)
        items=patt.findall(adc)
        for i  in  items:
            i=i.replace('</span>','').replace('<span>','').replace('<br/>','')
            i=i.strip()
            print(i)
qiushi=Qiushi()
jieguo=qiushi.qingshi(1)
qiushi.guolv(jieguo)
#第三步  保存的权限  和格式
