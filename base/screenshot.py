'''
窗口截图
'''
# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(2)

#截取当前窗口，并指定保存位置
try:
    picture = driver.get_screenshot_as_file('C:\\DownLoad\\baidu.png')
    print("%s:截图成功" % picture)
except BaseException as msg:
    print(msg)

driver.quit()