#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import allure
import configparser
import os
import time
import unittest
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#大模块
@allure.feature('Test Baidu WebUI')
class ISelenium(unittest.TestCase):
    # 读入配置文件
    def get_config(self):
        config = configparser.ConfigParser()
        if (platform.system() == 'Windows'):
            print(os.environ['HOMEPATH'])
            config.read(os.path.join(os.environ['HOMEPATH'], 'iselenium.ini'))
        elif (platform.system() == 'Linux'):
            config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        else:
            config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))

        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        # config = self.get_config()
        selenium_url = "http://106.14.90.243:8082/wd/hub"
        chrome_capabilities = {
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True,
        }

        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Remote(selenium_url, desired_capabilities=chrome_capabilities, options=chrome_options)

    @allure.story('Test key word 今日头条')
    def test_webui_1(self):
        """ 测试用例1，验证'今日头条'关键词在百度上的搜索结果
        """

        self._test_baidu('今日头条', 'test_webui_1')

    @allure.story('Test key word 王者荣耀')
    def test_webui_2(self):
        """ 测试用例2， 验证'王者荣耀'关键词在百度上的搜索结果
        """

        self._test_baidu('王者荣耀', 'test_webui_2')

    def _test_baidu(self, search_keyword, testcase_name):
        """ 测试百度搜索子函数

        :param search_keyword: 搜索关键词 (str)
        :param testcase_name: 测试用例名 (str)
        """

        self.driver.get("https://www.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(5)
        assert f'百度一下' in self.driver.title

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys("测试技术")
        elem.send_keys(f'{search_keyword}{Keys.RETURN}')
        time.sleep(2)
        # 通过关键字搜索结果后截图，并且以关键字命名图片
        self.driver.get_screenshot_as_file(f"./{search_keyword}.png")
        self.save_screenshot(f"./{search_keyword}.png", "测试用例截图")
        time.sleep(2)
        self.assertTrue(f'{search_keyword}' in self.driver.title, msg=f'{testcase_name}校验点 pass')

    def save_screenshot(self, file_name, img_doc):
        '''
        页面截屏保存截图
        :param file_name: 文件名称  img_doc截图说明
        :return:
        '''
        #self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)


