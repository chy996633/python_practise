#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-08-09 03:03:44
# Project: zhihuspider

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        "headers":{
            "Proxy-Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Accept": "*/*",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"
        }
    }

    @every(seconds=10)
    def on_start(self):
        self.crawl('https://www.zhihu.com/search?type=content&q=%E7%90%85%E7%90%8A%E6%A6%9C',callback=self.index_page)
    
    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            print(each)
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

