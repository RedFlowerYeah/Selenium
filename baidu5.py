'''
调用javascript进行元素的操作
'''

from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#设置窗口大小
driver.set_window_size(600,600)

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450)"
driver.execute_script(js)
sleep(3)

driver.quit()