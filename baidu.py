from selenium import webdriver

#连接到浏览器
driver=webdriver.Chrome()

#访问百度首页
first_url='http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

#访问百度新闻页
second_url='http://news.baidu.com'
print("now access %s" %(second_url))

#返回到百度首页
print("back to %s" %(first_url))
driver.back()

#前进到新闻页
print("forward to %s" %(second_url))
driver.forward()

driver.quit()