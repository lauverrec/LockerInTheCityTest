CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL,
    caloric_value INTEGER NOT NULL,
    saturated_fats DECIMAL(5,2) NOT NULL,
    sugar DECIMAL(5,2) NOT NULL
);

CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    opening_hours VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL
);

CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(id),
    store_id INTEGER NOT NULL REFERENCES stores(id),
    price DECIMAL(10,2) NOT NULL
);