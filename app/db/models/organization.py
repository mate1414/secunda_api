from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)

    building = relationship("Building", back_populates="organizations")
    phone_numbers = relationship("OrganizationPhone", back_populates="organization")
    activity_associations = relationship("OrganizationActivity", back_populates="organization")

    @property
    def activities(self):
        return [assoc.activity for assoc in self.activity_associations]

class OrganizationActivity(Base):
    __tablename__ = "organization_activities"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), primary_key=True)

    organization = relationship("Organization", back_populates="activity_associations")
    activity = relationship("Activity", back_populates="organization_associations")


class OrganizationPhone(Base):
    __tablename__ = "organization_phones"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    phone_number = Column(String(50), nullable=False, primary_key=True)

    organization = relationship("Organization", back_populates="phone_numbers")