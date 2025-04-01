from pydantic import BaseModel

# Schemas para Product
class ProductBase(BaseModel):
    brand: str
    product_type: str
    caloric_value: int
    saturated_fats: float
    sugar: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

# Schemas para Store
class StoreBase(BaseModel):
    name: str
    address: str
    opening_hours: str
    city: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    class Config:
        orm_mode = True

# Schemas para Price
class PriceBase(BaseModel):
    product_id: int
    store_id: int
    price: float

class PriceCreate(PriceBase):
    pass

class Price(PriceBase):
    id: int
    class Config:
        orm_mode = True
