import pandas as pd
import requests

URL_BASE = "http://127.0.0.1:8000"
HEADERS = {
    "Content-Type": "application/json"
}

#Products
products = pd.read_csv("products.csv")

for product in products.itertuples():
    
    payload = {
        "brand": product.brand,
        "product_type": product.product_type,
        "caloric_value": product.caloric_value,
        "saturated_fats": product.saturated_fats,
        "sugar": product.sugar
    }

    #call API
    response = requests.post(f"{URL_BASE}/products", json=payload, headers=HEADERS)

    if response.status_code == 400:
        print(f"The product already exists: {product.brand} {product.product_type}")
    elif response.status_code == 200:
        print(f"Product added: {product.brand} {product.product_type}")
    else:
        print(f"An error occurred when adding product: {response.text}")

#Stores
stores = pd.read_csv("stores.csv")

for store in stores.itertuples():
    
    payload = {
        "name": store.name,
        "address": store.address,
        "opening_hours": store.opening_hours,
        "city": store.city
    }

    #call API
    response = requests.post(f"{URL_BASE}/stores", json=payload, headers=HEADERS)

    if response.status_code == 400:
        print(f"The store already exists: {store.name} en {store.city}")
    elif response.status_code == 200:
        print(f"Store added: {store.name} en {store.city}")
    else:
        print(f"An error occurred when adding store: {response.text}")

#Prices
prices = pd.read_csv("prices.csv")

for price in prices.itertuples():
    
    payload = {
        "product_id": price.product_id,
        "store_id": price.store_id,
        "price": price.price
    }

    #call API
    response = requests.post(f"{URL_BASE}/prices", json=payload, headers=HEADERS)

    if response.status_code == 400:
        print(f"Price has already assigned.")
    elif response.status_code == 200:
        print(f"Price added.")
    else:
        print(f"An error occurred when assigning price: {response.text}")