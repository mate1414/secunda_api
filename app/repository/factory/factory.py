from app.database import get_db
from app.repository.organization import OrganizationRepository
from app.repository.building import BuildingRepository
from sqlalchemy.orm import Session
from fastapi import Depends

class RepositoryFactory:
    def __init__(self, db_session):
        self.db_session = db_session

    @property
    def organization(self):
        return OrganizationRepository(self.db_session)

    @property
    def building(self):
        return BuildingRepository(self.db_session)


def get_repository_factory(db: Session = Depends(get_db)):
    return RepositoryFactory(db)