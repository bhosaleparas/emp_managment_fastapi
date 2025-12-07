# pydantic scehmas for request and responce

from pydantic import BaseModel, EmailStr
from typing import Optional



# schema for creating employee
class EmployeeCreate(BaseModel):
    name:str
    email:EmailStr
    department:Optional[str]=None
    positin:Optional[str]=None
    salary:Optional[float]=None

    


# schema for getting employeee
class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:str
    department:Optional[str]
    position:Optional[str]
    salary:Optional[float]
    
    class Config:
        from_attributes=True



# schemas for updating employee
class EmployeeUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    department:Optional[str]=None
    position:Optional[str]=None
    salary:Optional[float]=None
    
    
