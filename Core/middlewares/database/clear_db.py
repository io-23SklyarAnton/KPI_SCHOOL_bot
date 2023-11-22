from Core.middlewares.database import connect


def drop_database():
    connection = connect.create_connection()

    if connection is not None:
        cursor = connection.cursor()

        create_db_query = "DROP DATABASE IF EXISTS kpi_school_bot"
        cursor.execute(create_db_query)
        connection.commit()
    else:
        return "fail to connect"


if __name__ == "__main__":
    drop_database()
