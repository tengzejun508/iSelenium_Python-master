#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver

selenium_url = "http://106.14.90.243:8082/wd/hub"               #selenium的访问地址
access_url = "http://www.baidu.com"                             #测试地址

chrome_capabilities ={
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
browser = webdriver.Remote(selenium_url, desired_capabilities=chrome_capabilities)
browser.get(access_url)
browser.get_screenshot_as_file("./baidu.png")  #把访问结果截图保存到当前路径的selenium/baidu.png
browser.quit()
