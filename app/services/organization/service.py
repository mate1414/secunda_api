from app.repository.factory.factory import RepositoryFactory
from app.db.models import Organization
from app.services.building.service import BuildingService


class OrganizationService:

    def get_multi_by_activity(
        self,
        activity_id: float,
        repo_factory: RepositoryFactory
    ) -> list[Organization] | None:
        pass

    @staticmethod
    def get_organizations_by_map_point_in_radius(
        latitude: float,
        longitude: float,
        radius_km: float,
        repo_factory: RepositoryFactory,
    ):
        organizations = repo_factory.organization.get_multi()

        organizations_in_radius = []
        for org in organizations:
            if BuildingService.is_building_in_radius(
                    latitude,
                    longitude,
                    org.building,
                    radius_km,
            ):
                organizations_in_radius.append(org)

        return organizations_in_radius
