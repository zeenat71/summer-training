import re
from typing import Optional
from pydantic import field_validator
from sqlmodel import SQLModel, Field


class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    condition: str
    risk_score: int
    active: bool = True

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str

# ----Create Schema   ----

class PatientCreate(SQLModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=120)
    condition: str = Field(min_length=1)
    risk_score: int = Field(ge=0, le=100)
    active: bool = True 


class PatientRead(SQLModel):
    id: int
    name: str
    age: int
    condition: str
    risk_score: int
    active: bool    

class PatientUpdate(SQLModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    age: Optional[int] = Field(default=None, ge=0, le=120)
    condition: Optional[str] = Field(default=None, min_length=1)
    risk_score: Optional[int] = Field(default=None, ge=0, le=100)
    active: Optional[bool] = None    


class UserCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit.")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")

        return value    


class UserRead(SQLModel):
    id: int
    username: str