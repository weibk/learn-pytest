#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/08 19:36

import requests


class InterfaceOp(object):
    @staticmethod
    def changeimg(data1):
        rep = requests.post(url='http://localhost:8080/HKR/UserServlet'
                                '?method=changePicture',
                            data=str(data1))
        result = rep.json()
        return result
