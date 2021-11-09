#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/08 19:36

import requests
import re


class InterfaceOp(object):
    @staticmethod
    def changeimg(data1, except1, pid):
        rep = requests.post(url='http://localhost:8080/HKR/UserServlet',
                            data=data1)
        text = rep.text
        if text.__contains__(except1) and rep.status_code == 200:
            uid = re.search('{"uid": "(.*?)","pid":pid}', text)[1]
            rep = requests.post(url='http://localhost:8080/HKR/UserServlet'
                                    '?method=changePicture',
                                data=str({'uid': uid, 'pid': pid}))
            if rep.status_code == 200:
                result = rep.json()
                return result['status']
            else:
                print("test failed changeimg")
        else:
            print("test failed login")
