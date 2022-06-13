from scripts.string_manipulation import transformWord
import pymysql

# --------------------------
# Prerequisites DB connection
# --------------------------

my_host = "localhost"
my_user="ecommerceapp"
my_password="ecommerceapp"
my_db="full-stack-ecommerce"

db_conn = pymysql.connect(host=my_host, user=my_user, password=my_password, db=my_db)
db_cursor = db_conn.cursor()
    
# --------------------------
# Function Queries
# --------------------------

def get_all_fields_from_db():
    result = []

    # Db query
    db_cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='product'")

    # Get data from query
    data_tuple = db_cursor.fetchall()

    # Return only field names
    for row in data_tuple:
        result.append(transformWord(row[3]))

    return result

def get_nr_products_from_db():
    result = 0
    db_cursor.execute("SELECT COUNT(*) FROM product")
    data_tuple = db_cursor.fetchall()                   

    result = data_tuple[0][0]           # db returned a tuple matrix 
    return result