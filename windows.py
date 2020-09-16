from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获取百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

#获取当前所有打开的窗口的句柄
all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('now register windows!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)
        #......

#回到搜索窗口
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('now search window!')
        driver.find_element_by_id('TANGRAM_PSP_2_closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)

driver.quit()