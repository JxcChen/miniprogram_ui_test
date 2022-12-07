# -*- coding:utf-8 -*-
# @Time     :2022/7/30 12:20 下午
# @Author   :CHNJX
# @File     :main_page.py
# @Desc     :app主页
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from base.app import App
from page.report_page import ReportPage


class MainPage(App):
    def into_report_page(self) -> ReportPage:
        """
        报事页面
        """
        self.find_and_click(MobileBy.XPATH, "//wx-button")
        self.switch_windows(':VISIBLE')
        return ReportPage(self.driver)

    def init_mini_main_page(self):
        """
        进入小程序首页
        :return: 当前页面
        """

        self.find_and_click(MobileBy.XPATH, "//*[@text='发现']") \
            .find_and_click(MobileBy.XPATH, "//*[@text='小程序']") \
            .find_and_click(MobileBy.XPATH, "//*[@text='想家友邻']")
        sleep(5)
        self.switch_context('WEBVIEW_com.tencent.mm:appbrand0')
        self.switch_windows(':VISIBLE')
        return self

    def back_to_main_page(self):
        self.switch_context('WEBVIEW_com.tencent.mm:appbrand0')
        self.switch_windows(':VISIBLE')
        try:
            self.logger.info('返回小程序首页')
            self.wait_for_visible((By.CSS_SELECTOR, '.top_logo'), 3)
        except Exception as e:
            # 先切换会原生app
            self.switch_context('NATIVE_APP')
            self.swap_back().back_to_main_page()
            self.switch_context('WEBVIEW_com.tencent.mm:appbrand0')
        return self
