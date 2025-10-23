from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, index=True)
    parent_id = Column(Integer, ForeignKey("activities.id"), nullable=True)

    children = relationship(
        "Activity",
        backref=backref("parent", remote_side="Activity.id"),
        cascade="all, delete-orphan"
    )

    organization_associations = relationship("OrganizationActivity", back_populates="activity")