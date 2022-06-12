from getgauge.python import step, before_scenario, Messages
from numpy import product
from api_calls.backend.products_api_calls import *
from database.db_queries import *


# --------------------------
# Prerequisites step implementations
# --------------------------
my_host = "localhost"
my_user="ecommerceapp"
my_password="ecommerceapp"
my_db="full-stack-ecommerce"

# Get all column names of "products" table, but delete categoryId and lastUpdated for now
all_column_names = get_all_fields_from_db(my_host, my_user, my_password, my_db);
all_column_names.remove("categoryId")   # api calls doesn't contain it
all_column_names.remove("lastUpdated")  # didn't implement update functionalities

# --------------------------
# Gauge step implementations
# --------------------------

@step("Product has all fields.")
def check_product_has_all_fields():
    # Api call to get a random product
    res = get_random_product()

    # Assert status code is 200 OK
    assert res.status_code == 200, "Status CODE is different from 200 OK, it is " + str(res.status_code)

    # Assert fields exist and are not null
    for it in all_column_names:
        if type(res.json()[it]) is str:
            assert len(res.json()[it]) > 0, res.json()[it] + " is null, please recheck database"
        elif type(res.json()[it]) is int:
            assert res.json()[it] != 0, str(res.json()[it]) + " is wrong, please recheck database"
        elif type(res.json()[it]) is bool:
            assert res.json()[it] is True, "Active field is " + str(res.json()[it])

@step("Total number of products is correct.")
def check_total_nr_of_products_is_correct():
    # Api call to get the all products
    res = get_all_products_of_each_category()

    # print(len(res.json()["_embedded"]["products"]))
    # print(res.json()["_embedded"]["products"])
    # print(len(res.json()["_embedded"]["productCategory"]))
    # print(len(res))

    # NEFINALIZAT !!!!!!!!!!

# ---------------
# Execution Hooks (before_scenario functions)
# ---------------