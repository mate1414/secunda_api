from sqlalchemy.orm import Session

from sqlalchemy.orm import aliased, joinedload
from sqlalchemy import select, literal, and_
from app.repository.repository import BaseRepository
from app.db import models
from app.db.models.organization import Organization


class OrganizationRepository(BaseRepository):
    """
    Репозиторий для получения записей из таблицы 'organizations'
    """

    def __init__(self, db: Session):
        super().__init__(models.Organization, db)

    def get_one(self, organization_id) -> Organization | None:
        return self.db.query(self.model).filter_by(id=organization_id).one_or_none()

    def get_multi(self) -> list[Organization] | None:
        return self.db.query(self.model).all()

    def get_multi_by_building_id(self, building_id) -> list[Organization] | None:
        return self.db.query(self.model).filter_by(building_id=building_id).all()

    def get_multi_by_activity(self, activity_id) -> list[Organization] | None:
        return self.db.query(self.model).filter_by(activity_id=activity_id).all()

    def get_multi_by_activity_recursive(
            self,
            activity_id: int,
            max_depth: int = 3,
    ) -> list[Organization]:
        activity_tree = (
            select(
                models.Activity.id,
                models.Activity.name,
                literal(0).label('depth')
            )
            .where(models.Activity.id == activity_id)
            .cte(name='activity_tree', recursive=True)
        )

        activity_alias = aliased(models.Activity, name='a')

        recursive_part = (
            select(
                activity_alias.id,
                activity_alias.name,
                (activity_tree.c.depth + 1).label('depth')
            )
            .where(
                and_(
                    activity_alias.parent_id == activity_tree.c.id,
                    activity_tree.c.depth < max_depth - 1
                )
            )
        )

        activity_tree = activity_tree.union_all(recursive_part)

        # Основной запрос с организациями
        organizations = (
            self.db.query(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.phone_numbers),
                joinedload(Organization.activity_associations).joinedload(
                    models.OrganizationActivity.activity
                )
            )
            .join(models.OrganizationActivity)
            .join(activity_tree, models.OrganizationActivity.activity_id == activity_tree.c.id)
            .all()
        )

        return organizations