import datetime
from Core.middlewares.database import connect


def insert_user(user_id: int, first_name: str) -> (str, None):
    try:
        connection = connect.create_connection("kpi_school_bot")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users "
                       "(user_id, first_name) "
                       "VALUES (%s, %s);", (user_id, first_name))
        connection.commit()
        return "User has been added successfully"
    except connect.Error as enter_user_data_error:
        print(f"fail to write user data: {enter_user_data_error}")
        return


def insert_file(user_id: int, file_id: str, send_date: datetime.datetime, file_type: str, description: str = "") -> str:
    try:
        connection = connect.create_connection("kpi_school_bot")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO files "
                       "(file_id, description, file_type) "
                       "VALUES (%s, %s, %s)", (file_id, description, file_type))
        cursor.execute("INSERT INTO file_user "
                       "(user_id, file_id, send_date) "
                       "VALUES (%s, %s, %s);", (user_id, file_id, send_date))
        connection.commit()
        return "File <b>has been</b> added <i>successfully</i>"
    except connect.Error as enter_user_data_error:
        print(f"fail to write file data: {enter_user_data_error}")
        return "File <b>hasn't been</b> added"
