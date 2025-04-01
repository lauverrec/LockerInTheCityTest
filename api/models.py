from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from databaseConnection import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    product_type = Column(String(100), nullable=False)
    caloric_value = Column(Integer, nullable=False)
    saturated_fats = Column(Float, nullable=False)
    sugar = Column(Float, nullable=False)
    
    __table_args__ = (UniqueConstraint('brand', 'product_type', name='uix_brand_type'),)
    
    prices = relationship("Price", back_populates="product")

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    opening_hours = Column(String(50), nullable=False)
    city = Column(String(100), nullable=False)

    __table_args__ = (UniqueConstraint('name', 'city', name='uix_name_city'),)
    
    prices = relationship("Price", back_populates="store")

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    price = Column(Float, nullable=False)

    __table_args__ = (UniqueConstraint('product_id', 'store_id', name='uix_product_store'),)
    
    product = relationship("Product", back_populates="prices")
    store = relationship("Store", back_populates="prices")
