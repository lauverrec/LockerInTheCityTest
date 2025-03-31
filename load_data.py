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
        "type": product.type,
        "caloric_value": product.caloric_value,
        "saturated_fats": product.saturated_fats,
        "sugar": product.sugar
    }

    #call API
    response = requests.post("http://127.0.0.1:8000/products", json=payload, headers=HEADERS)

    if response.status_code == 201:
        print("POST realizado correctamente. Respuesta:")
        print(response.json())
    else:
        print(f"Error en la petición POST: {response.status_code}")

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
    response = requests.post("http://127.0.0.1:8000/stores", json=payload, headers=HEADERS)

    if response.status_code == 201:
        print("POST realizado correctamente. Respuesta:")
        print(response.json())
    else:
        print(f"Error en la petición POST: {response.status_code}")

#Prices
prices = pd.read_csv("prices.csv")

for price in prices.itertuples():
    
    payload = {
        "product_id": price.product_id,
        "store_id": price.store_id,
        "price": price.price
    }

    #call API
    response = requests.post("http://127.0.0.1:8000/prices", json=payload, headers=HEADERS)

    if response.status_code == 201:
        print("POST realizado correctamente. Respuesta:")
        print(response.json())
    else:
        print(f"Error en la petición POST: {response.status_code}")