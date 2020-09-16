from xml.dom import minidom

#打开xml文档
dom=minidom.parse('D:\\LearingSelenium\\info.xml')
#得到文档对象
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)