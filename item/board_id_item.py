# coding=utf-8

import scrapy


class board_id_item(scrapy.Item):
    id = scrapy.Field()
    city_name = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    size_type = scrapy.Field()
    sn = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = "insert into board_id(id,city_name,longitude,latitude,size_type,sn) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (
            self["id"], self["city_name"], self["longitude"], self["latitude"],
            self["size_type"], self["sn"])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from board_id where id =%s"""
        params = (self["id"])
        return query, params
