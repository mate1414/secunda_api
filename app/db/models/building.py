from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False, unique=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(Text, nullable=True)

    organizations = relationship("Organization", back_populates="building")
