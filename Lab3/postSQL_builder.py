from query_builder import QueryBuilder

class PostSQLBuilder(QueryBuilder):
    def select(self, columns: list) -> 'PostSQLBuilder':
        # Метод для вибору колонок в PostSQL
        self.query["select"] = ", ".join(columns)
        return self

    def where(self, condition: str) -> 'PostSQLBuilder':
        # Метод для додавання умови WHERE в PostSQL
        self.query["where"] = condition
        return self

    def limit(self, limit: int) -> 'PostSQLBuilder':
        # Метод для обмеження кількості результатів в PostSQL
        self.query["limit"] = limit
        return self

    def getSQL(self) -> str:
        # Метод для генерації SQL запиту в форматі PostSQL
        sql = f"SELECT {self.query['select']} FROM table_name"

        if self.query["where"]:
            sql += f" WHERE {self.query['where']}"

        if self.query["limit"]:
            sql += f" LIMIT {self.query['limit']}"

        return sql + ";"