from xml.dom import minidom

#打开xml文档
dom = minidom.parse('D:\\LearingSelenium\\info.xml')

#得到文档元素对象
root = dom.documentElement

provinces = dom.getElementsByTagName('province')
cities = dom.getElementsByTagName('city')

#获取第二个province标签对的值
p2 = provinces[1].firstChild.data
print(p2)

#获得第一个city标签对的值
c1 = cities[0].firstChild.data
print(c1)

#获得第二个city标签对的值
c2 = cities[1].firstChild.data
print(c2)