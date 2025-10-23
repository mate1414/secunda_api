from pydantic import BaseModel

from app.schemas.activity import Activity
from app.schemas.building import Building

class OrganizationPhone(BaseModel):
    phone_number: str

    class Config:
        from_attributes = True


class Organization(BaseModel):
    id: int
    name: str
    building: Building
    phone_numbers: list[OrganizationPhone]
    activities: list[Activity]

    class Config:
        from_attributes = True
