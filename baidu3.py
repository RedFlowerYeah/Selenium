#键盘事件,通过send_keys（）方法模拟键盘输入或组合键的输入
import time

from selenium import webdriver
#引入key类（键盘类）
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")

time.sleep(5)
#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

time.sleep(5)
#输入空格+"教程"
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")

time.sleep(5)
#ctrl+a全选输入框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')

time.sleep(5)
#ctrl+x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

time.sleep(5)
#ctrl+c黏贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')

time.sleep(5)
#通过回车键来代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(1)
driver.quit()