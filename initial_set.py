import pandas as pd 

products = [
    {"id": 1, "brand": "BrandA", "type": "Snack", "caloric_value": 150, "saturated_fats": 10, "sugar": 5},
    {"id": 2, "brand": "BrandB", "type": "Drink", "caloric_value": 200, "saturated_fats": 0, "sugar": 25},
]

stores = [
    {"id": 1, "name": "SupermarketX", "address": "123 Main St", "opening_hours": "08:00-21:00", "city": "CityA"},
    {"id": 2, "name": "StoreY", "address": "456 Avenue", "opening_hours": "09:00-20:00", "city": "CityB"},
]

prices = [
    {"product_id": 1, "store_id": 1, "price": 2.5},
    {"product_id": 1, "store_id": 2, "price": 2.7},
    {"product_id": 2, "store_id": 1, "price": 1.5},
    {"product_id": 2, "store_id": 2, "price": 1.7},
]

def generate_csv_files():
    # Create DataFrames for each dataset
    df_products = pd.DataFrame(products)
    df_stores = pd.DataFrame(stores)
    df_prices = pd.DataFrame(prices)

    # Export DataFrames to CSV files
    df_products.to_csv("products.csv", index=False, encoding="utf-8")
    df_stores.to_csv("stores.csv", index=False, encoding="utf-8")
    df_prices.to_csv("prices.csv", index=False, encoding="utf-8")
    
    print("CSV files generated successfully.")

if __name__ == "__main__":
    generate_csv_files()