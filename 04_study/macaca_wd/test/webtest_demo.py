#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__author__ = 'zishuai'
__mtime__ = '18/2/18'

              ┏┓   ┏┓
             ┏┛┻━━━┛┻┓
             ┃   ☃    ┃
             ┃ ┳┛  ┗┳  ┃
             ┃    ┻    ┃
             ┗━┓      ┏━┛
              ┃       ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
'''
import unittest
import time
from macaca import WebDriver


desired_caps = {
    'platformName': 'desktop',
    'browserName': 'electron'
    # 'version': '11',
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_url(self):
        self.driver.set_window_size(860, 600).get('https://www.baidu.com')

    def test_search_macaca(self):
        self.driver.element_by_id('kw').send_keys('macaca')
        self.driver.element_by_id('su').click()
        time.sleep(3)
        html = self.driver.source
        self.assertTrue('macaca' in html)
        self.assertTrue(self.driver.element_by_css_selector_if_exists('#head > div.head_wrapper'))
        self.driver.element_by_xpath_or_none('//*[@id="kw"]').send_keys(' elementByXPath')
        self.driver.element_by_id('su').click()
        self.driver.save_screenshot('./screen.png')


if __name__ == '__main__':
    unittest.main()
