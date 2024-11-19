from query_builder import QueryBuilder

class PostSQLBuilder(QueryBuilder):
    def select(self, columns: list) -> 'PostSQLBuilder':
        self.query["select"] = ", ".join(columns)
        return self

    def where(self, condition: str) -> 'PostSQLBuilder':
        self.query["where"] = condition
        return self

    def limit(self, limit: int) -> 'PostSQLBuilder':
        self.query["limit"] = limit
        return self

    def getSQL(self) -> str:
        sql = f"SELECT {self.query['select']} FROM table_name"

        if self.query["where"]:
            sql += f" WHERE {self.query['where']}"

        if self.query["limit"]:
            sql += f" LIMIT {self.query['limit']}"

        return sql + ";"