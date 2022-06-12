from scripts.string_manipulation import transformWord
import pymysql

def get_all_fields_from_db(my_host, my_user, my_password, my_db):
    result = []
    # Db conn and query
    db_conn = pymysql.connect(host=my_host, user=my_user, password=my_password, db=my_db)
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='product'")

    # Get data from query
    data = db_cursor.fetchall()

    # Return only field names
    for row in data:
        result.append(transformWord(row[3]))

    return result