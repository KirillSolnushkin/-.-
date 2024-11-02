from query_builder import QueryBuilder

class MySQLBuilder(QueryBuilder):
    def select(self, columns: list) -> 'MySQLBuilder':
        # Метод для вибору колонок в MySQL
        self.query["select"] = ", ".join(columns)
        return self

    def where(self, condition: str) -> 'MySQLBuilder':
        # Метод для додавання умови WHERE в MySQL
        self.query["where"] = condition
        return self

    def limit(self, limit: int) -> 'MySQLBuilder':
        # Метод для обмеження кількості результатів в MySQL
        self.query["limit"] = limit
        return self

    def getSQL(self) -> str:
        # Метод для генерації SQL запиту в форматі MySQL
        sql = f"SELECT {self.query['select']} FROM table_name"

        if self.query["where"]:
            sql += f" WHERE {self.query['where']}"

        if self.query["limit"]:
            sql += f" LIMIT {self.query['limit']}"

        return sql + ";"