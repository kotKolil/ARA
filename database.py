# Importing external classes
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

# Importing local classes
from settings import DBName

SQLALCHEMY_DATABASE_URL = f"sqlite:///./{DBName}.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Creating the base class for models
class Base(DeclarativeBase):
    pass

# Defining the Product model
class Product(Base):

    __tablename__ = "products" 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    customer = Column(String)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
else:
    session = sessionmaker(autoflush=False, bind=engine)
    db = session()