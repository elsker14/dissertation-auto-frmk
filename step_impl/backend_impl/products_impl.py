from getgauge.python import step, before_scenario, Messages
from numpy import product
from api_calls.backend.products_api_calls import *
from database.db_queries import *


# --------------------------
# Prerequisites step implementations
# --------------------------


# Get all column names of "products" table, but delete categoryId and lastUpdated for now
all_column_names = get_all_fields_from_db();
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
    res_api = get_nr_of_products_from_each_category()

    # Db call to get all products
    res_db = get_nr_products_from_db()

    # Assert what backend returns is equal to what is in db
    assert res_api == res_db, "Backend returns a different total number of products than database"

@step("Searching for a word through products <table>")
def check_if_word_exist(table):
    searched_words = table.get_column_values_with_name("Word")
    expected_statuses = table.get_column_values_with_name("Status")

    i = 0
    for i in range(len(searched_words)):
        res_bool = search_word(searched_words[i])
        assert expected_statuses[i] == res_bool, "The word: " + searched_words[i] + ", that should be " + expected_statuses[i] + " was found " + res_bool

# ---------------
# Execution Hooks (before_scenario functions)
# ---------------