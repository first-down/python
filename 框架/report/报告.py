#!/usr/bin/ env python
# -*- encoding:utf-8 -*-
# import HTMLTestRunnertest
from 框架.driver.运行 import Test_run
from 框架.data.读取_数据 import 文件
# from 框架.config.学校_接口 import 学校_查询
class gun():
    def tes_1(self):
        Test_run.run_多个()
    def tes_2(self):
        Test_run.run_all()
if __name__=='__main__':
    # run=Test_run()
    aa=文件()
    if 'all' in aa:
        Test_run().run_all()
    else:
        Test_run().run_多个(aa)
