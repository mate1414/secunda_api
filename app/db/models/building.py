from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Text


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)

    address = Column(String(500), nullable=False, unique=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
