#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-23 20:52:12
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-23 20:52:12
from logger.logger import logger
HOST = {
    "QA": "www.baidu.com",
    "UAT": "www.baidu.com",
    "PRODUCTION": "www.baidu.com"
}


@logger
def getHost(env):
    if isinstance(env, str):
        env = env.upper()
        for k in HOST:
            if k == env:
                return HOST.get(k)
    else:
        return None
