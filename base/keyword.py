#参数化搜索关键字
from selenium import webdriver
import time

#创建一个数组来存放搜索关键字
search_text=['python','中文','text']

#通过for遍历数组
for text in search_text:
    driver=webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(text)
    driver.find_element_by_id('su').click()
    time.sleep(5)
    driver.quit()