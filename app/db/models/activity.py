from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Activity(Base):
    __tablename__ = "activities"

    name = Column(String(200), nullable=False, index=True)
    parent_id = Column(Integer, ForeignKey("activities.id"), nullable=True)

    children = relationship("Activity", back_populates="parent")
    parent = relationship("Activity", back_populates="children")

    organizations = relationship("OrganizationActivity", back_populates="activity")