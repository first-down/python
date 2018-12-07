#/usr/bin/env python
#-*- coding:utf-8 -*-
import xlrd
def tes_数据():
    shuju = []
    f = xlrd.open_workbook(r'c:\Users\幸存者\Desktop\nnt\框架\data\test.xlsx')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1, num):
        aaa = sheet.row_values((i))
        shuju.append(aaa)
    return (shuju)
def 文件():
    with open('a.txt','r+') as f:
        aa=f.readlines()
        return aa
