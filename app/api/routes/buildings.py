from fastapi import APIRouter, HTTPException, Depends
from app.services.building.service import BuildingService
from app.repository.factory.factory import RepositoryFactory, get_repository_factory
from app.schemas.geo import RadiusSearch
from app.schemas.building import Building

router = APIRouter(prefix="/buildings")


@router.get("/by-map-point/radius", response_model=list[Building])
def search_buildings_in_radius(
    search: RadiusSearch,
    repo_factory: RepositoryFactory = Depends(get_repository_factory)
) -> list[dict[str, str]]:
    buildings = BuildingService.get_buildings_by_map_point_in_radius(
        search.latitude,
        search.longitude,
        search.radius_km,
        repo_factory,
    )

    if not buildings:
        raise HTTPException(status_code=404, detail="Not found")

    return [
        Building.model_validate(building).model_dump()
        for building in buildings
    ]
