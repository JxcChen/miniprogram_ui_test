# -*- coding:utf-8 -*-
# @Time     :2022/7/30 12:21 下午
# @Author   :CHNJX
# @File     :test_report.py
# @Desc     :app测试用例
import random

from base.app import App
from page.main_page import MainPage
from project_logger import ProjectLogger


class TestDemo:
    logger = ProjectLogger().get_logger()
    def setup_class(self):
        self.main = MainPage().init_mini_main_page()

    def test_report_success(self):
        self.logger.info('测试正常报事流程')
        report_name = str(random.randint(100, 500)) + "测试一下"
        assert self.main.into_report_page().report(report_name).get_report_success_result(report_name)

    def test_report_without_content(self):
        self.logger.info('测试报事不输入报事内容')
        res = self.main.into_report_page().report_without_content()
        assert len(res)

    def teardown(self):
        self.main.back_to_main_page()
