# coding: utf-8

from selenium import webdriver
import time
url = "http://jp-bigdata-00:8080/"
driver = webdriver.Firefox()
# # 无窗口浏览器，设置窗口，使其可以完整绘图
# driver.set_window_size(800, 600)
driver.get(url)
for i in range(70):
    elem = driver.find_element_by_css_selector("#container-blog > div > div:nth-child(2) > div.post-title.underline.clearfix > h1 > a")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_css_selector("#blog > nav > div > div.navbar-header > a")
    elem.click()
