from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from databaseConnection import SessionLocal, engine, Base
import models, schemas

# Create the tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint for adding a new product
@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_db = db.query(models.Product).filter(
        models.Product.brand == product.brand,
        models.Product.product_type == product.product_type
    ).first()

    if product_db:
        raise HTTPException(status_code=400, detail="The product has already created")
    
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Endpoint for updating a product
@app.put("/products/{product_id}", response_model=schemas.ProductCreate)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db_product.caloric_value = product.caloric_value
    db_product.saturated_fats = product.saturated_fats
    db_product.sugar = product.sugar
    db.commit()
    db.refresh(db_product)
    return schemas.ProductCreate(
        brand=db_product.brand,
        product_type=db_product.product_type,
        caloric_value=db_product.caloric_value,
        saturated_fats=float(db_product.saturated_fats),
        sugar=float(db_product.sugar)
    )

# Endpoint for adding a new store
@app.post("/stores", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    store_db = db.query(models.Store).filter(
        models.Store.name == store.name,
        models.Store.city == store.city
    ).first()
    
    if store_db:
        raise HTTPException(status_code=400, detail="This store has already created in this city")
    
    new_store = models.Store(**store.dict())
    db.add(new_store)
    db.commit()
    db.refresh(new_store)
    return new_store

# Endpoint for assigning a price to a product in a store
@app.post("/prices")
def create_price(price_data: schemas.PriceCreate, db: Session = Depends(get_db)):
    # Search the product
    product_db = db.query(models.Product).filter(
        models.Product.id == price_data.product_id
    ).first()

    if not product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Search the store
    store_db = db.query(models.Store).filter(
        models.Store.id == price_data.store_id
    ).first()

    if not store_db:
        raise HTTPException(status_code=404, detail="Store not found")
    
    price_db = db.query(models.Price).filter(
        models.Price.product_id == product_db.id,
        models.Price.store_id == store_db.id
    ).first()

    if price_db:
        if price_db.price != price_data.price:
            price_db.price = price_data.price
            db.commit()
            db.refresh(price_db)
        else:
            raise HTTPException(status_code=400, detail="This price has already created to this product in this store")
    else:
        price = models.Price(product_id=price_data.product_id, store_id=price_data.store_id, price=price_data.price)
        db.add(price)
        db.commit()
        db.refresh(price)
    
    return {"Price assign correctly"}

# Endpoint for getting all products of a store
@app.get("/stores/{store_id}/products", response_model=list[schemas.Product])
def get_products_by_store(store_id: int, db: Session = Depends(get_db)):
    db_est = db.query(models.Store).filter(models.Store.id == store_id).first()
    
    if not db_est:
        raise HTTPException(status_code=404, detail="Store not found")
    
    products = db.query(models.Product).join(models.Price, models.Product.id == models.Price.product_id)\
                .filter(models.Price.store_id == store_id).all()
    
    return products
