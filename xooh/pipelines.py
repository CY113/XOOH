# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

import pymysql
from scrapy.utils.project import get_project_settings


class XoohPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']
        # 连接数据库
        self.connect = pymysql.connect(host=self.host, db=self.db,
                                       user=self.user, passwd=self.passwd,
                                       charset='utf8',
                                       use_unicode=False)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            sql, params = item.distinct_data()
            self.cursor.execute(sql, params)
            data = self.cursor.fetchone()
            # 数据去重
            if data:
                pass
            else:
                # 插入数据
                sql, params = item.get_insert_sql()
                self.cursor.execute(sql, params)
                self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item

class XoohMongoDBPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings["MONGODB_HOST"]
        self.port = self.settings["MONGODB_PORT"]
        self.dbname = self.settings["MONGODB_DBNAME"]
        self.sheetname = self.settings["MONGODB_SHEETNAME"]
        client = pymongo.MongoClient(host=self.host, port=self.port)
        mydb = client[self.dbname]
        self.post = mydb[self.sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item