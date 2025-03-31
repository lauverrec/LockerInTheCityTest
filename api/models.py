from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database1 import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    caloric_value = Column(Integer, nullable=False)
    saturated_fats = Column(Float, nullable=False)
    sugar = Column(Float, nullable=False)
    
    prices = relationship("Price", back_populates="product")

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    opening_hours = Column(String(50), nullable=False)
    city = Column(String(100), nullable=False)
    
    prices = relationship("Price", back_populates="store")

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    price = Column(Float, nullable=False)
    
    product = relationship("Product", back_populates="prices")
    store = relationship("Store", back_populates="prices")
