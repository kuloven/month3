import sqlite3
from .queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        # connect = sqlite3.connect(self.path)
        # контекстный менеджер
        with sqlite3.connect(self.path) as connect:
            connect.execute(Queries.CREATE_REVIEW_TABLE)
            connect.execute(Queries.DROP_CATEGORY_OF_DISHES_TABLE)
            connect.execute(Queries.CREATE_CATEGORY_OF_DISHES_TABLE)
            connect.execute(Queries.CREATE_DISHES_TABLE)
            connect.execute(Queries.INSERT_INTO_DISHES)
            connect.execute(Queries.INSERT_INTO_CAT)

            connect.commit()

    def execute(self, query: str, params: tuple = None):
        with sqlite3.connect(self.path) as connect:
            connect.execute(query, params)

    def fetch(self, query: str, params: tuple = None, fetchmany: bool = True):
        with sqlite3.connect(self.path) as connect:
            result = connect.execute(query,params)

            return result.fetchall()