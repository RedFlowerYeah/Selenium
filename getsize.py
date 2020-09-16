from selenium import webdriver

#连接到浏览器
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#获取输入框的尺寸
size=driver.find_element_by_id('kw').size
print(size)

#返回百度页面底部备案信息
text=driver.find_element_by_id('cp').text
print(text)

#返回元素的属性值，可以使id,name,type或其他属性任意值
attribute=driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#返回的元素的结果是否可见，返回结果为true或false
result=driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()