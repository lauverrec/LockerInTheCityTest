from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database1 import SessionLocal, engine, Base
import models, schemas

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para agregar un nuevo producto
@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Endpoint para actualizar un producto existente
@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

# Endpoint para agregar un nuevo establecimiento
@app.post("/stores/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    db_store = models.Store(**store.dict())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

# Endpoint para asignar un precio a un producto en un establecimiento
@app.post("/prices/", response_model=schemas.Price)
def create_price(price: schemas.PriceCreate, db: Session = Depends(get_db)):
    db_price = models.Price(**price.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

# Endpoint para obtener todos los productos de un establecimiento
@app.get("/stores/{store_id}/products", response_model=list[schemas.Product])
def get_products_by_store(store_id: int, db: Session = Depends(get_db)):
    # Se consulta la tabla de precios para obtener los productos asociados al establecimiento
    prices = db.query(models.Price).filter(models.Price.store_id == store_id).all()
    if not prices:
        raise HTTPException(status_code=404, detail="Store not found or no products available")
    product_ids = [p.product_id for p in prices]
    products = db.query(models.Product).filter(models.Product.id.in_(product_ids)).all()
    return products
