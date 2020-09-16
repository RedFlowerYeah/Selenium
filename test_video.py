'''
处理html5视频的播放
'''

from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.videojs.com")

video=driver.find_element_by_xpath("body/Setion[1]/div/video")

'''
JavaScript里面的内置的对象叫arguments，currentSrc返回当前视频的url
load、play、pause这些表示视频的加载、播放和暂停
'''
#返回播放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15秒钟
time.sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)

driver.quit()