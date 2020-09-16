from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#显式等待
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#WebDriverWait（driver:浏览器驱动
# timeout:最长超过时间
# 检测的时间间隔，默认0.5s
# 抛出异常）
#一般配合unitl使用
element=WebDriverWait(driver,5,0.5).until(
    EC.presence_of_element_located((By.ID,"kw"))
)

element.send_keys('selenium')
driver.quit()