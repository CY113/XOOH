# -*- coding: utf-8 -*-
import json

import scrapy

from item.board_id_item import board_id_item
from querydata.QueryCityId import QueryCityId


class BoardIdSpider(scrapy.Spider):
    name = 'board_id'

    def __init__(self):
        self.url = "http://www.xooh.com/board/list?city={}&page={}"
        self.page = 1

    def start_requests(self):
        city_id = QueryCityId().get_city_id()
        for num in range(1,len(city_id)+1):
            # 后续需要无pages参数的url，所以两次格式化 city 和 pages
            start_url = self.url.format(city_id[num][0], '{}')
            final_url = start_url.format(self.page)
            yield scrapy.Request(url=final_url, callback=self.parse,
                                 meta={'page': self.page,
                                       'start_url': start_url})

    def parse(self, response):

        item = board_id_item()
        result = json.loads(response.body.decode())
        id_list = result['data']
        pages = result['pages']
        item['city_name'] = result['city_name']
        # 判断当前页数是否大于该城市数据总页数
        if response.meta['page'] <= pages:
            for num in range(len(id_list)):
                item["id"] = id_list[num]["id"]  # ID
                item["longitude"] = id_list[num]["longitude"]  # 经度
                item["latitude"] = id_list[num]["latitude"]  # 纬度
                item["size_type"] = id_list[num]["size_type"]  # 尺寸类型
                item["sn"] = id_list[num]["sn"]  # 编号
                yield item
            # 翻页
            current_page = response.meta['page'] + 1
            # 获取不带页数参数的url
            start_url = response.meta['start_url']
            # 请求下一页请求
            yield scrapy.Request(url=start_url.format(current_page),
                                 callback=self.parse,
                                 meta={'page': current_page,
                                       'start_url': start_url})
