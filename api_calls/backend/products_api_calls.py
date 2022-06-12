from email.mime import base
from random import randrange
from numpy import base_repr
import requests

base_url = "http://localhost:8080/api"

def get_random_product():
    product_id = randrange(1, 100)
    res = requests.get(base_url + "/products/" + str(product_id))

    return res

# somehow wrong, don't use it
def get_all_products():
    res = requests.get(base_url + "/products")

    return res

def get_all_categories():
    res = requests.get(base_url + "/product-category")

    return res

# nefinalizat, not working
def get_all_products_of_each_category():
    res_categ = get_all_categories()
    nr_of_categ = len(res_categ.json()["_embedded"]["productCategory"])
    result = dict()
    for it in range(nr_of_categ):
        res_tmp = requests.get(base_url + "/products/search/findByCategoryId?id=" + str(it + 1))
        result.update(res_tmp.json()["_embedded"])
    
    return result