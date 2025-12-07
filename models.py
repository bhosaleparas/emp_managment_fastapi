from sqlalchemy import Column, Integer, String, Float
from database import Base


class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True,index=True)
    department=Column(String)
    position=Column(String)
    salary=Column(Float)
    