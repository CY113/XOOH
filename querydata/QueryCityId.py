# coding=utf-8
from tools import DBHelper


class QueryCityId(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_city_id(self):
        # 查询目标ID
        self.db_helper.connect_database()
        query_sql = "SELECT city_id FROM city_id ORDER BY city_id"
        return self.db_helper.query_task(query_sql)


if __name__ == '__main__':
    query = QueryCityId()
    print(query.get_city_id())
