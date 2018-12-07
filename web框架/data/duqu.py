from selenium import webdriver
from time import sleep
from web框架.config.jiben import we
dr=webdriver.Chrome()
import xlrd
class duqu():
    def wenjian(self):
        ad=xlrd.open_workbook('web测试.xlsx','r+')
        sheet=ad.sheets()[0]
        rn=[]
        a=sheet.nrows
        for i in range(1,a):
            tt=sheet.row_values((i))
            rn.append(tt)
        return rn
