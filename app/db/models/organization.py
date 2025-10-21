from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Organization(Base):
    __tablename__ = "organizations"

    name = Column(String(200), nullable=False, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)

    building = relationship("Building")
    activities = relationship("OrganizationActivity", back_populates="organization")

    phone_numbers = relationship("OrganizationPhone", back_populates="organization")


class OrganizationActivity(Base):
    __tablename__ = "organization_activities"

    organization_id = Column(Integer, ForeignKey("organizations.id"), primary_key=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), primary_key=True)

    organization = relationship("Organization", back_populates="activities")
    activity = relationship("Activity", back_populates="organizations")
