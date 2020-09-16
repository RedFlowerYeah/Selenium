from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#sleep的使用 sleep表示固定的休眠事件
sleep(2)
driver.find_element_by_id("kw").send_keys("webdriver")
driver.find_element_by_id("su").click()

sleep(3)
driver.quit()