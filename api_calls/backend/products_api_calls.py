from email.mime import base
from random import randrange
from numpy import base_repr, product
import requests

base_url = "http://localhost:8080/api"

def get_random_product():
    api_specific_url = "/products/"
    product_id = randrange(1, 100)
    res = requests.get(base_url + api_specific_url + str(product_id))

    return res

# somehow wrong, don't use it
def get_all_products():
    api_specific_url = "/products"
    res = requests.get(base_url + api_specific_url)

    return res

def get_all_categories():
    api_specific_url = "/product-category"
    res = requests.get(base_url + api_specific_url)

    return res

def get_nr_of_products_from_each_category():
    # Get all categories in db
    res_categ = get_all_categories()
    nr_of_categ = len(res_categ.json()["_embedded"]["productCategory"])

    # Get nr of products by summing how many are in each category
    result = 0
    for it in range(nr_of_categ):
        res_tmp = requests.get(base_url + "/products/search/findByCategoryId?id=" + str(it + 1))
        result = result + res_tmp.json()["page"]["totalElements"]
        
    return result

def search_word(searched_word):
    api_specific_url = "/products/search/findByNameContaining?name=";
    res = requests.get(base_url + api_specific_url + searched_word)

    if res.json()["page"]["totalElements"] > 0:
        found = "true"
    else:
        found = "false"

    return found