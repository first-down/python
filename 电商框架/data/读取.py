import xlrd
def  ssl():
    shuju=[]
    ad=xlrd.open_workbook(r'c:\Users\幸存者\Desktop\nnt\电商框架\data\duqu.xlsx')
    sheet=ad.sheets()[0]
    c=sheet.nrows
    for i in range(c):
        tt=sheet.row_values((i))
        shuju.append(tt)
    return shuju
def 文件():
    with open(r'c:\Users\幸存者\Desktop\nnt\电商框架\data\qaq.txt','r+') as f:
        tt=f.readlines()
        return tt
# print(文件())
