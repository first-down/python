import requests
# import re
# url1='http://www.doutula.com/article/list/?page=1'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'}
# response=requests.get(url=url1,headers=head)
# html=response.content.decode('UTF-8')
# # print(html)
# patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# items=patt.findall(html)
# print(items)
# for i in items:
#     respons=requests.get(url=i,headers=head)
#     html1 = respons.content.decode('utf-8')
#     patt1=re.compile(r'<img src="https://ws(.*?)alt')
#     items1=patt1.findall(html1)
#     for j,i in enumerate(items1):
#         i=i.replace('"','')
#         i='http://ws'+i
#         #print(i)
#         a=requests.get(i)
#         res1=a.content
#         print(res1)
#         with open('{}.jpg'.format(j),'wb')as f:
#             f.write(res1)
#

# import os
# for i in range(11):
#     os.remove('{}.jpg'.format(i))


# #简单点的
# import requests
# import re
# url='https://book.douban.com/latest?icn=index-latestbook-all'
# heard={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# res=requests.get(url=url,headers=heard)
# html=res.content.decode('utf-8')
# print(html)
# pattern=re.compile(r'><img src="(.*?)"/></a>',re.S)
# pattern1=re.compile(r'a href="https://book.douban.com/subject/[0-9]{8}/">(.*?)</a>',re.S)
# items=pattern.findall(html)
# items1=pattern1.findall(html)
# print(items)
# for j,i in enumerate(items):
#     new_url=i
#     respons=requests.get(url=new_url,headers=heard)
#     tu=respons.content
#     with open(r'C:\Users\幸存者\Desktop\{}.jpg'.format(items1[j]),'wb') as f:
#             f.write(tu)






# import re
# import requests
# import os
# def wangzhi():
#     url='https://www.doutula.com/article/list/?page=3'
#     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#     res=requests.get(url=url,headers=head)
#     html=res.content.decode('UTF-8')
#     patt=re.compile(r'https://www.doutula.com/article/detail/[0-9]{7}',re.S)
#     items=patt.findall(html)
#     return items
# a=wangzhi()
# # print(a)
# def baocun(b):
#     for q,i in enumerate(b):
#         i=i.replace( '">' ,'')
#         os.mkdir(r'C:\Users\doungin\Desktop\新建文件夹{}'.format(q))
#         # print(i)
#         url=i
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#         res = requests.get(url=url, headers=head)
#         html1 = res.content.decode('UTF-8')
#         patt1 = re.compile(r'onerror="this.src=(.*?)"', re.S)
#         items1=patt1.findall(html1)
#         # print(items1)
#         for k,j in enumerate(items1):
#             j=j.replace(',','')
#             j=j.replace("'",'')
#             tupian = requests.get(j)
#             res1 = tupian.content
#             with open(r'C:\Users\doungin\Desktop\新建文件夹{}\{}.jpg'.format(q,k), 'wb') as f:
#                 f.write(res1)
# baocun(a)

#
# import requests
# import re
# import time
# url='http://www.mmjpg.com/'
# querystring = {"home":"2"}
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# response=requests.request("get",url=url,headers=headers,verify=False, params=querystring)
# html=response.content.decode('UTF-8')
# patt=re.compile('http://fm.shiyunjj.com/small/2018/[0-9]{4}.jpg')
# itmes=patt.findall(html)
# print(itmes)
# for i,j in enumerate(itmes):
#     j_new=j
#     time.sleep(5)
#     responses=requests.get(url=j_new,headers=headers,verify=False,params=querystring)
#     htmll=responses.content
#     with open(r'C:\Users\幸存者\Desktop\大侄子\{}.gif   '.format(i),'wb') as f:
#         f.write(htmll)



# import time
# a=input('请输入年月日')
# b=a.split(' ')
# c=time.strptime('{} {} {}'.format(int(b[0]),int(b[1]),int(b[2])),'%Y %m %d')
# if c[0]%4==0 and c[0]%100!=0 or c[0]%400==0:
#     print('这是个瑞年{}，今年的第{}天，星期{}'.format(c[0],c[-2],c[-3]+1))
# else:
#     print('这不是是个瑞年{}，今年的第{}天，星期{}'.format(c[0], c[-2], c[-3] + 1))
# #


import time
class shuchu():
    def shuru(self,a,b,c):
        c = time.strptime('{} {} {}'.format(a,b,c), '%Y %m %d')
        if c[0]%4==0 and c[0]%100!=0 or c[0]%400==0:
            return('这是个瑞年{}，今年的第{}天，星期{}'.format(c[0],c[-2],c[-3]+1))
        else:
            return('这不是是个瑞年{}，今年的第{}天，星期{}'.format(c[0], c[-2], c[-3] + 1))


print(time.strftime('%Y %m %d  %H-%M-%S',time.localtime(time.time())))

