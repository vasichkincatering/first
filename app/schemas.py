from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class LeadBase(BaseModel):
    name: str
    phone: str
    email: EmailStr
    event_date: date
    guests_count: int
    source: Optional[str] = None
    status: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    event_date: Optional[date] = None
    guests_count: Optional[int] = None
    source: Optional[str] = None
    status: Optional[str] = None


class LeadRead(LeadBase):
    id: int

    class Config:
        orm_mode = True
