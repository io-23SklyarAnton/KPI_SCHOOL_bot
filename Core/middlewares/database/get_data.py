from Core.middlewares.database import connect
from typing import List


def return_last_files(user_id: int, amount: int) -> (List[tuple], None):
    try:
        connection = connect.create_connection("kpi_school_bot")
        cursor = connection.cursor()

        cursor.execute("SELECT f.file_type, f_u.file_id, f.description,f_u.send_date "
                       "FROM file_user f_u "
                       "JOIN files f "
                       "ON f.file_id = f_u.file_id "
                       "WHERE f_u.user_id = %s "
                       "ORDER BY f_u.send_date DESC "
                       "LIMIT %s;", (user_id, amount))
        user_files = cursor.fetchall()
        return user_files
    except connect.Error as enter_user_data_error:
        print(f"fail to write user data: {enter_user_data_error}")
        return


def return_file(user_id: int, description: str) -> (List[tuple], None):
    try:
        connection = connect.create_connection("kpi_school_bot")
        cursor = connection.cursor()

        cursor.execute("SELECT f.file_type, f_u.file_id "
                       "FROM file_user f_u "
                       "JOIN files f "
                       "ON f.file_id = f_u.file_id "
                       "WHERE f_u.user_id = %s "
                       "AND f.description = %s "
                       "ORDER BY f_u.send_date DESC;", (user_id, description))
        user_files = cursor.fetchall()
        return user_files
    except connect.Error as enter_user_data_error:
        print(f"fail to write user data: {enter_user_data_error}")
        return
