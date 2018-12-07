
#/usr/bin/env python
# -*- coding:utf-8 _*-
import unittest
import  HTMLTestRunnertest
from 框架.hao_test.test_学校 import 学校
import time
class Test_run():
    def run_多个(self,aa):
            suit=unittest.TestSuite()
            for a in aa:
                disvover = unittest.defaultTestLoader.discover(r'..\hao_test', pattern='{}.py'.format(a.strip()))
                suit.addTest(disvover)
            now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
            f=open('adc.html','wb')
            runner=HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
                                                         description='测试结果如下：',
                                                         title='好分数测试报告',
                                                         stream=f)
            runner.run(suit)
            f.close()
    def run_all(self):    #
            suit=unittest.TestSuite()
            disvover=unittest.defaultTestLoader.discover(r'..\hao_test',pattern='test*.py')   #第一个需要测试的文件
            suit.addTest(disvover)
            print(disvover)
            now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
            f = open('adcd.html', 'wb')
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='幸存者',
                                                       description='测试结果如下：',
                                                       title='好分数测试报告',
                                                       stream=f)
            runner.run(suit)
            f.close()



# if __name__=='__main__':
#     run=Test_run()
#     with open('a.txt','r+') as f:
#         aa=f.readlines()
#         print(aa)
#
#     if 'all' in aa:
#         run.run_all()
#     else:
#         run.run_多个(aa)
