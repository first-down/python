#/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import requests
from 框架.config.学校_接口 import 学校_查询
from 框架.data.读取_数据 import tes_数据
class 学校(unittest.TestCase):
    tes_1=学校_查询().学校_快查
    shuju = tes_数据()
    def test_1(self):
        html = self.tes_1(self.shuju[0][0])
        self.assertEqual(html['code'], int(self.shuju[0][1]))
        self.assertEqual(len(html['data']), 702)
        self.assertEqual(html['data'][0]['schoolId1.5'], -1)
    def test_2(self):
        html = self.tes_1(self.shuju[1][0])
        self.assertNotEqual(html['code'], int(self.shuju[1][1]))
    def test_3(self):
        html = self.tes_1(self.shuju[2][0])
        self.assertEqual(html['code'], int(self.shuju[2][1]))
        self.assertIsNotNone(html)

