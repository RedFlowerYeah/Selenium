from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

time.sleep(5)
#鼠标悬停至“设置”链接,用xpath定位方式
link =driver.find_element_by_xpath("//span[@id='s-usersetting-top']")
#用的是ActionChains里面的move_to_element的鼠标悬停方法
ActionChains(driver).move_to_element(link).perform()

#打开搜索设置
driver.find_element_by_link_text("搜索设置").click()

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

#接收警告框
ale=driver.switch_to.alert
ale.accept()
print("已完成警告框的处理")

driver.quit()