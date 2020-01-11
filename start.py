# -*- coding: utf-8 -*-
# !/usr/bin/python3
"""
爬虫启动类
"""
from scrapy.cmdline import execute
# execute(['scrapy', 'run'])
execute(['scrapy', 'run', '-p', '2', '5'])
