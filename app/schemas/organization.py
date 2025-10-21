from pydantic import BaseModel
from typing import List
from datetime import datetime

from app.schemas.activity import ActivitySimple


class OrganizationBase(BaseModel):
    name: str


class BuildingSimple(BaseModel):
    id: int
    address: str
    latitude: float
    longitude: float


class Organization(OrganizationBase):
    id: int
    building: BuildingSimple
    phone_numbers: List[str]
    activities: List[ActivitySimple]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrganizationList(BaseModel):
    items: List[Organization]
    total: int
