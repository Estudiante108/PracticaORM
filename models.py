from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db import Base

class Store(Base):
    __tablename__ = "Store"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Employee(Base):
    __tablename__ = "Employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Inventory(Base):
    __tablename__ = "Inventory"

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("store.id"))
    employee_id = Column(Integer,ForeignKey("Employee.id"))
    date = Column(Date)
    flavor = Column(String(50))
    is_season_flavor = Column(Boolean)
    quantity = Column(Integer)

