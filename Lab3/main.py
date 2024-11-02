from mySQL_builder import MySQLBuilder
from postSQL_builder import PostSQLBuilder

def main():
    mysql_builder = MySQLBuilder()
    mysql_query = mysql_builder \
        .select(["id", "name", "email"]) \
        .where("age > 18") \
        .limit(10) \
        .getSQL()
    print("MySQL:")
    print(mysql_query)

    postgresql_builder = PostSQLBuilder()
    postgresql_query = postgresql_builder \
        .select(["id", "name", "email"]) \
        .where("age > 18") \
        .limit(10) \
        .getSQL()
    print("\nPostSQL:")
    print(postgresql_query)


if __name__ == "__main__":
    main()