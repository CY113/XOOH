# coding=utf-8
from tools import DBHelper


class QueryBoardId(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_board_sn(self):
        # 查询目标ID
        self.db_helper.connect_database()
        query_sql = "SELECT sn FROM board_id ORDER BY id"
        return self.db_helper.query_task(query_sql)


if __name__ == '__main__':
    query = QueryBoardId()
    print(query.get_board_sn())
