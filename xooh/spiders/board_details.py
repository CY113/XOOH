# -*- coding: utf-8 -*-
import json

import scrapy

from item.board_details_item import board_details_item
from querydata.QueryBoardId import QueryBoardId


class BoardIdSpider(scrapy.Spider):
    name = 'board_details'

    def __init__(self):
        self.url = "http://www.xooh.com/board/detail?sn={}"

    def start_requests(self):
        # 获取广告屏ID
        board_sn_list = QueryBoardId().get_board_sn()
        for num in range(len(board_sn_list)):
            start_url = self.url.format(board_sn_list[num][0])
            yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        item = board_details_item()
        result = json.loads(response.body.decode())
        item['id'] = result['id']  # ID
        item['sn'] = result['sn']  # 编号
        item['name'] = result['name'].strip('\n')  # 名称
        item['price'] = result['price']  # 价格
        item['price_discount'] = result['price_discount']  # 折扣价
        item['price_dealer'] = result['price_dealer']  # 成交价
        item['cover'] = result['cover']  # 封面地址
        item['import_cover_name'] = result['import_cover_name']  # 封面名称
        item['import_video_name'] = result['import_video_name']  # 视频名称
        item['video'] = result['video']  # 视频地址
        item['city'] = result['city']  # 城市
        item['district'] = result['district']  # 市区
        item['town'] = result['town']  # 城镇
        item['bmap_resolved'] = result['bmap_resolved']
        item['longitude'] = result['longitude']  # 经度
        item['latitude'] = result['latitude']  # 纬度
        item['address'] = result['address'].strip('\n')  # 详细地址
        item['orientation_intro'] = result['orientation_intro']
        item['wight'] = result['wight']  # 屏幕宽度
        item['hight'] = result['hight']  # 屏幕高度
        item['show_wight'] = result['show_wight']
        item['show_hight'] = result['show_hight']
        item['floor_hight'] = result['floor_hight']
        item['type'] = result['type']  # 广告牌类型
        item['show_type'] = result['show_type']  # 展示类型
        item['begin_show_time'] = result['begin_show_time']  # 有效展示开始时间
        item['end_show_time'] = result['end_show_time']  # 有效展示结束时间
        item['show_time_text'] = result['show_time_text']  # 单次播放时长
        item['ferer_time'] = result['ferer_time']
        item['show_times'] = result['show_times']  # 展示人次
        item['show_times_people'] = result['show_times_people']  # 日人流量
        item['show_times_car'] = result['show_times_car']  # 日车流量
        item['sound_intro'] = result['sound_intro']  # 音响环境
        item['around_intro'] = result['around_intro']  # 媒体环境
        item['min_buy_time'] = result['min_buy_time']  # 收费计量标准
        item['confirm_time'] = result['confirm_time']
        item['complete_time'] = result['complete_time']
        item['intro'] = result['intro']
        item['keyword'] = result['keyword']
        item['position_point'] = result['position_point']
        item['use_trade'] = result['use_trade']  # 适用行业
        item['total_point'] = result['total_point']
        item['comment_point'] = result['comment_point']
        item['ctime'] = result['ctime']
        item['mtime'] = result['mtime']
        item['option_user'] = result['option_user']
        item['last_option_user'] = result['last_option_user']
        item['company_id'] = result['company_id']  # 公司ID
        item['company'] = result['company']  # 公司名称
        item['server_name'] = result['server_name']  # 联系人
        item['company_intro'] = result['company_intro']  # 公司介绍
        item['server_phone'] = result['server_phone']  # 联系电话
        item['trade_type'] = result['trade_type']  # 交易类型
        item['is_recomm'] = result['is_recomm']
        item['is_deleted'] = result['is_deleted']
        item['pre_sn'] = result['pre_sn']
        item['dimension'] = result['dimension']
        item['display_area'] = result['display_area']  # 展示面积
        item['source_type'] = result['source_type']
        item['screens'] = result['screens']
        item['remarks'] = result['remarks']
        item['prohibition'] = result['prohibition']
        item['material'] = result['material']
        item['points'] = result['points']
        item['ground_clearance'] = result['ground_clearance']
        item['lamplight'] = result['lamplight']
        item['process_cost'] = result['process_cost']
        item['point_chosemore'] = result['point_chosemore']
        item['points_min'] = result['points_min']
        item['disable_decision'] = result['disable_decision']
        item['status'] = result['status']
        item['orientation'] = result['orientation']
        item['size_type'] = result['size_type']  # 广告牌尺寸
        item['orientation_text'] = result['orientation_text']
        item['type_text'] = result['type_text']  # 广告牌类型
        item['show_type_text'] = result['show_type_text']
        item['favorite'] = result['favorite']  # 收藏数
        item['trades'] = result['trades']  # 媒体类型
        try:
            item['_show_time'] = result['_show_time']
        except:
            item['_show_time'] = ""
        item['errno'] = result['errno']
        item['errmsg'] = result['errmsg']
        yield item
