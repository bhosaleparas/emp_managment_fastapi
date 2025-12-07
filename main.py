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

@app.get('/employee/{emp_id}',response_model=schemas.EmployeeResponse)
def get_employee(employee_id:int ,db:Session=Depends(get_db)):
    employee=db.query(models.Employee).filter(models.Employee.id==employee_id).first()
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"employee not found for is {employee_id}"
        )
    
    return employee


@app.put('/employees/{emp_id}',response_model=schemas.EmployeeResponse)
def update_employee(emp_id:int,employee_update:schemas.EmployeeUpdate,db:Session=Depends(get_db)):
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"employee not found for is {emp_id}"
        )
        
    # if email is updated check if new emil exist or not
    
    if employee_update.email and employee_update.email !=db_employee:
        exiisting_employee=db.query(models.Employee).filter(models.Employee.email==employee_update.email).first()
        
        if exiisting_employee:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        
        # update employee
        update_data=employee_update.model_dump(exclude_unset=True)
        for field,value in update_data.items():
            if value is not None:
                setattr(db_employee,field,value)
                
        db.commit()
        db.refresh(db_employee)
        return db_employee
    
    
    
# delete employee
@app.delete('/employees/{emp_id}')
def delete_employee(emp_id:int,db:Session=Depends(get_db)):
    employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"employee not found for is {emp_id}"
        )
        
        
    db.delete(employee)
    db.commit()
    
    return {"message":f"employee with id {emp_id} deleted successfully"}




# Search employees by department
@app.get("/employees/search/department/{department}")
def search_by_department(department: str, db: Session = Depends(get_db)):
    employees = db.query(models.Employee).filter(
        models.Employee.department.ilike(f"%{department}%")
    ).all()
    
    return employees




# Search employees by name
@app.get("/employees/search/name/{name}")
def search_by_name(name: str, db: Session = Depends(get_db)):
    employees = db.query(models.Employee).filter(
        models.Employee.name.ilike(f"%{name}%")
    ).all()
    
    return employees