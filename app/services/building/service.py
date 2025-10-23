from app.repository.factory.factory import RepositoryFactory
from app.services.utils import calculate_distance
from app.db.models import Building


class BuildingService:

    @staticmethod
    def get_buildings_by_map_point_in_radius(
        latitude: float,
        longitude: float,
        radius_km: float,
        repo_factory: RepositoryFactory,
    ):
        buildings = repo_factory.building.get_multi()

        buildings_in_radius = []
        for building in buildings:
            if BuildingService.is_building_in_radius(latitude, longitude, building, radius_km):
                buildings_in_radius.append(building)

        return buildings_in_radius

    @staticmethod
    def is_building_in_radius(latitude: float, longitude: float, building: Building, radius_km: float) -> bool:
        distance = calculate_distance(
            latitude, longitude,
            building.latitude, building.longitude
        )

        if distance <= radius_km:
            return True

        return False
