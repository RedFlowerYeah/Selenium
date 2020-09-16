from selenium import webdriver
import os,time

'''
利用Xpath和css找到页面元素
'''
driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('checkbox.html')
driver.get(file_path)

'''
通过Xpath找到type=checkbox的元素
checkboxes=driver.find_elements_by_tag_name("//input[@type='checkbox']")
'''

#通过css元素来找到type=checkbox的元素
checkboxes=driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    print("找到input元素")
    time.sleep(1)

#打印在当前页面上type为checkbox的元素个数
print(len(checkboxes))

#把页面上最后1个checkbox的钩给去掉
'''
若是想勾选某一个元素数值，
pop(0)，默认取一组元素中的第一个
pop(1)，默认取一组元素中的第二个
'''
driver.find_elements_by_css_selector('input[type=checkbox]').pop(0).click()

time.sleep(2)
driver.quit()