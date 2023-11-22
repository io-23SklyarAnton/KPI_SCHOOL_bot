from Core.middlewares.database import connect


def create_database():
    connection = connect.create_connection()

    if connection is not None:
        cursor = connection.cursor()

        create_db_query = "CREATE DATABASE IF NOT EXISTS kpi_school_bot"
        cursor.execute(create_db_query)
        connection.commit()
    else:
        return "fail to connect"


def create_tables():
    connection = connect.create_connection()
    cursor = connection.cursor()

    try:
        use_db_query = "USE kpi_school_bot"
        cursor.execute(use_db_query)
        create_users_table_query = "CREATE TABLE IF NOT EXISTS users(" \
                                   "user_id INTEGER primary key," \
                                   "first_name varchar(30))"
        create_files_table_query = "CREATE TABLE IF NOT EXISTS files(" \
                                   "file_id varchar(100) primary key, " \
                                   "description varchar(100), " \
                                   "file_type varchar(30))"
        create_file_user_table_query = "CREATE TABLE IF NOT EXISTS file_user(" \
                                       "user_id INTEGER, " \
                                       "file_id varchar(100)," \
                                       "send_date datetime," \
                                       "FOREIGN KEY (user_id) REFERENCES users(user_id)," \
                                       "FOREIGN KEY (file_id) REFERENCES files(file_id))"

        cursor.execute(create_users_table_query)
        cursor.execute(create_files_table_query)
        cursor.execute(create_file_user_table_query)
        connection.commit()
    except connect.Error as db_connect_error:
        print(f"Oops, there is an error: {db_connect_error}")


if __name__ == "__main__":
    create_database()
    create_tables()
