from query_builder import QueryBuilder

class MySQLBuilder(QueryBuilder):
    def select(self, columns: list) -> 'MySQLBuilder':
        self.query["select"] = ", ".join(columns)
        return self

    def where(self, condition: str) -> 'MySQLBuilder':
        self.query["where"] = condition
        return self

    def limit(self, limit: int) -> 'MySQLBuilder':
        self.query["limit"] = limit
        return self

    def getSQL(self) -> str:
        sql = f"SELECT {self.query['select']} FROM table_name"

        if self.query["where"]:
            sql += f" WHERE {self.query['where']}"

        if self.query["limit"]:
            sql += f" LIMIT {self.query['limit']}"

        return sql + ";"