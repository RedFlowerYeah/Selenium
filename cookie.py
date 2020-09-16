'''
WebDriver给我们提供给了操作cookie的相关方法，可以读取、添加和删除cookie信息
WebDriver操作cookie的方法：
get_cookie():       获取所有cookie信息
get_cookie():       返回字典的key为“name”的cookie信息
add_cockie(cookie_dict):    添加cookie。“cookie_dict”指字典对象，必须有name和value值
delete_cookie(name,optionsString):      删除cookie信息，“name”是要删除的cookie的名称，“optionsString”是该cookie的选项
delete_all_cookies():   删除所有cookie信息
'''

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

#获取cookie信息
cookie=driver.get_cookies()

#将获取的cookie信息打印
print(cookie)

driver.quit()