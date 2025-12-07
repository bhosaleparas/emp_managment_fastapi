from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List


# import modules

import models
import schemas
from database import engine,get_db


# create a tables in db
models.Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Employee Mangement API",
    description="simple crud api"
)

@app.get('/')
def root():
    return {
        'messages':"Employee management api",
        "endpoints":{
            "GEt/employees":"get all emp",
            "/employees/{id}":"get emp by id",
            "POST/employees":"create new emp using post req",
            'PUT/employees/{id}':"update employee by id",
            'DELETE/employees/{id}':"delete emp by id"
        }
    }
    
    
#get all employeess

@app.get('/employees',response_model=List[schemas.EmployeeResponse])
def get_emp(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    employees=db.query(models.Employee).offset(skip).limit(limit).all()
    return employees


# create employees
@app.post('/employees',response_model=schemas.EmployeeResponse,status_code=status.HTTP_201_CREATED)
def create_emp(employee:schemas.EmployeeCreate,db:Session=Depends(get_db)):
    db_employee=db.query(models.Employee).filter(models.Employee.email==employee.email).first()
    if db_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email alredy registered"
        )
    
    new_empoyee=models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        position=employee.positin,
        salary=employee.salary
    )
    
    db.add(new_empoyee)
    db.commit()
    db.refresh(new_empoyee)
    return new_empoyee



# get emp by id
