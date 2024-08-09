from sqlalchemy import create_engine, columns,Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///parcolab.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__= "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

Base.Metadata.create_all(engine)
