# !/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/09 10:12

from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")
runner = HTMLTestRunner.HTMLTestRunner(
    title="汉科软系统测试报告",
    description="更换头像测试",
    verbosity=2,
    stream=open(file="hkr.html", mode="w", encoding="utf-8")
)
runner.run(tests)