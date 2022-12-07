# -*- coding:utf-8 -*-
# @Time     :2022/11/11 9:35 下午
# @Author   :CHNJX
# @File     :report_page.py
# @Desc     :报事页面
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from base.app import App

home_repair = (By.LINK_TEXT, "居家维修")
customer_service = (By.LINK_TEXT, "客户服务")
question_input = (By.XPATH, "//*[@id='content']/div/textarea")
commit_button = (MobileBy.XPATH, "//wx-button")
result_text = (By.XPATH, "//wx-text[@class='title']/span[2]")
go_home_button = (By.CSS_SELECTOR, 'wx-button')


# 不传报事内容错误控件


class ReportPage(App):

    def report(self, report_name):
        # 小程序要textarea才能进行输入操作
        self.find_and_send(report_name, question_input).find_and_click(commit_button).switch_windows(':VISIBLE')
        return self

    def report_without_content(self):
        self.find_and_click(commit_button).switch_context('NATIVE_APP')
        res = self.driver.window_handles
        return self.find_and_click(commit_button).switch_context('NATIVE_APP').find_element(MobileBy.XPATH,
                                                                "//@[text='请输入问题']")

    def get_report_success_result(self, report_name):
        res = self.find_element(*result_text).get_element_text()
        # 判断是否为判断成功 如果为提交成功 则继续往下  否则直接失败
        assert '提交成功' in res
        self.find_and_click(*go_home_button).switch_windows(':VISIBLE')
        sleep(2)
        self.find_elements(By.XPATH, f"//wx-view[text()='{report_name}']")
        return self._elements

    def get_report_fail_result(self, report_name):
        self.find_and_click(*go_home_button).switch_windows(':VISIBLE')
        sleep(2)
        self.find_elements(By.XPATH, f"//wx-view[text()='{report_name}']")
        return self._elements
