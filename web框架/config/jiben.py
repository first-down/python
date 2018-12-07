from selenium import webdriver
from time  import sleep
class lei():
    def we(slef):
        dr=webdriver.Firefox()
        dr.get('http://www.moore.ren/')
        dr.maximize_window()
        dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[1]/div[1]/div[1]/a').click()
        sleep(2)
        ff=dr.window_handles
        dr.switch_to_window(ff[-1])
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span').click()
        aa = dr.title
        return aa
print(lei().we())