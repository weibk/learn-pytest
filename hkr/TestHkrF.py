#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/09 09:42

import unittest
from DataHkr import DataPhoto
from InterfaceOp import InterfaceOp
from ddt import ddt, data, unpack


@ddt
class TestHkrF(unittest.TestCase):
    @data(*DataPhoto.dataf)
    @unpack
    def test_hkr(self, data1, except1):
        iop = InterfaceOp()
        result = iop.changeimg(data1)
        self.assertEqual(len(result), except1)
