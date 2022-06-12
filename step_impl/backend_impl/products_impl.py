from getgauge.python import step, before_scenario, Messages
import requests
import json

# --------------------------
# Prerequisites step implementations
# --------------------------

fields = [
    "id", 
    "sku", 
    "name", 
    "description", 
    "unitPrice", 
    "imageUrl",
    "active",
    "unitsInStock",
    "dateCreated",
    "lastUpdated"]

# --------------------------
# Gauge step implementations
# --------------------------

@step("Product has all fields.")
def check_product_has_all_fields():
    res = requests.get("http://localhost:8080/api/products")

    print(res.status_code)
    print("------------------")
    # print(res.content)

    print(res.json()["_embedded"]["products"][1]["name"]) 

# ---------------
# Execution Hooks (before_scenario functions)
# ---------------