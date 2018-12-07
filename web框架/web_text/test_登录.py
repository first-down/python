from web框架.config.jiben import lei
import HTMLTestRunnertest
from selenium import webdriver
import unittest
import time
# dr=webdriver.Firefox()
class TT(unittest.TestCase,lei):
    def test_1(self):
        a=self.we()
        self.assertEqual('数字芯片设计工程师招聘-华为海思招聘-摩尔精英招聘',a)
    # def text_2(self):

if __name__ =='__main__':
     unittest.main()

# import time
# a=input('请输入日期')
# b=a.split(' ')
# c=time.strptime('{} {} {}'.format(int(b[0]),int(b[1]),int(b[2])),'%Y %m %d')
# if  c[0]%4==0 and  c[0]%100 or c[0]%400==0:
#     print('{}是瑞年，是{}天，星期{}'.format(c[0],c[-2],c[-3]+1))
# else:
#     print('{}不是是瑞年，是{}天，星期{}'.format(c[0], c[-2], c[-3] + 1))
