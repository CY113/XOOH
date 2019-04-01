# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class XoohSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class XoohDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


proxy_list = [
    "http://60.188.45.85:4263",
    "http://112.195.140.101:4215",
    "http://125.107.218.82:4267",
    "http://60.179.109.248:4270",
    "http://112.194.69.117:4226",
    "http://182.100.238.245:9756",
    "http://112.84.244.101:6915",
    "http://182.37.104.20:6856",
    "http://122.230.242.98:4223",
    "http://125.111.149.227:4205",
    "http://117.28.66.151:4216",
    "http://114.230.147.52:4257",
    "http://183.156.245.79:4204",
    "http://60.160.57.126:4236",
    "http://182.110.228.69:5324",
    "http://117.94.68.27:5676",
    "http://122.237.80.116:5946",
    "http://182.34.144.69:4246",
    "http://124.152.185.8:2132",
    "http://115.207.120.26:7305",

]


class XoohHeadersMiddleware(object):
    def process_request(self, request, spider):
        # Headers中携带该参数，使数据变为json格式
        X = "XMLHttpRequest"
        request.headers['X-Requested-With'] = X


class XoohProxyMiddleware(object):
    def process_request(self, request, spider):
        ip = random.choice(proxy_list)
        request.meta['proxy'] = ip
        print(request.meta['proxy'])

    def process_response(self, request, response, spider):
        """对返回的response处理"""
        if response.status != 200:
            ip = random.choice(proxy_list)
            print("this is response ip:" + ip)
            request.meta['proxy'] = ip
            return request
        return response

    def process_exception(self, request, exception, spider):
        # 出现异常时（超时）使用代理
        print("\n出现异常，正在使用代理重试....\n")
        ip = random.choice(proxy_list)
        request.meta['proxy'] = ip
        return request
