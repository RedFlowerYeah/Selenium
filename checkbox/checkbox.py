from selenium import webdriver
import os,time

#通过tag_name查找页面中的元素
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

#选择页面上的所有的tag name为input的元素
inputs=driver.find_elements_by_tag_name('input')

#然后从中过滤出type为checkbox的元素，单机勾选
for i in inputs:
    if i.get_attribute('type')=='checkbox':
        i.click()
        print("找到input元素")
        time.sleep(1)

driver.quit()