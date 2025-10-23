from typing import Type, TypeVar
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository:
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db
