#tcp

# # #客户端
# import socket
# #创建socket 封装协议
# soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器     接收的也是元组
# soc.connect(('192.168.0.67',233))
# #发送请求
# aaa='黑暗终将到来'
# soc.send(aaa.encode('utf-8'))
# #接收响应
# msg=soc.recv(1024)
# print(msg.decode('utf-8'))


#udp
# import socket
# #创建socket  封装协议
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送数据
# a=('192.168.0.67',233)
# reg='lalalala'
# soc.sendto(reg.encode('utf-8'),a)
# #接收响应
# c=soc.recv(1024)
# print(c.decode('utf-8'))



# a=input('请输入')
# b=a.split(' ')
# for i in range(len(b)):
#     for j in range(i,len(b)):
#         if int(b[i])>int(b[j]):
#             b[i],b[j]=b[j],b[i]
#     print(b)



# import requests
# import re
# import urllib3
# urllib3.disable_warnings()
# url='https://www.dagumanhua.com/manhua/12687/'
#
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# response=requests.get(url=url,headers=headers,verify=False)
# html=response.content.decode('utf-8')
# patt=re.compile('<li><a href="(.*?)" title=')
# itmes=patt.findall(html)
# for i,j in enumerate(itmes):
#         j_new=j.replace('/manhua/','')
#         new='https://www.dagumanhua.com/manhua/'+j_new
#         res=requests.get(url=new,headers=headers,verify=False)
#         html1=res.content.decode('utf-8')
#
#         patt2=re.compile('<h1>(.*?)</h1>',re.S)   #这个是标题
#         itmes2=patt2.findall(html1)
#         patt1=re.compile('><img src="(.*?)"></a></p></div>')
#         itmes1=patt1.findall(html1)
#         print(itmes1)
#         for i in itmes1:
#             if i==[]:
#                 pass
#             else:
#                 a=requests.get(i)
#                 b=a.content
#                 with open(r'C:\Users\幸存者\Desktop\阿娇\{}.jpg'.format(itmes2),'wb') as f:
#                     f.write(b)
#
# patt3=re.compile('</a>&nbsp;<a href="(.*?)">')
# itmes3=patt3.findall(html1)
# for w,r in enumerate(itmes3):



