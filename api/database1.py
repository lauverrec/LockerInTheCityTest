from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cadena de conexión a MySQL (ajusta los valores según tu configuración)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:p%40ssword123%21@localhost:3306/products_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
