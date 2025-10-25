from fastapi import APIRouter, Depends, HTTPException, Query
from app.schemas.organization import Organization
from app.schemas.geo import RadiusSearch
from app.repository.factory.factory import RepositoryFactory, get_repository_factory
from app.services.organization.service import OrganizationService


router = APIRouter(prefix="/organizations")


@router.get("/{organization_id}", response_model=Organization)
def get_organization(
    organization_id: int,
    repo_factory: RepositoryFactory = Depends(get_repository_factory)
) -> dict[str, str]:
    organization = repo_factory.organization.get_one(organization_id)

    if not organization:
        raise HTTPException(status_code=404, detail="Not found")

    return Organization.model_validate(organization).model_dump()


@router.get("/by-building/{building_id}", response_model=list[Organization])
def get_organizations_by_building(
    building_id: int,
    repo_factory: RepositoryFactory = Depends(get_repository_factory)
) -> list[dict[str, str]]:
    organizations = repo_factory.organization.get_multi_by_building_id(building_id)
    if not organizations:
        raise HTTPException(status_code=404, detail="Not found")

    return [
        Organization.model_validate(organization).model_dump()
        for organization in organizations
    ]


@router.get("/by-map-point/radius", response_model=list[Organization])
def get_organizations_in_radius(
    search: RadiusSearch,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, str]]:
    organizations = OrganizationService.get_organizations_by_map_point_in_radius(
        search.latitude,
        search.longitude,
        search.radius_km,
        repo_factory,
    )

    if not organizations:
        raise HTTPException(status_code=404, detail="Not found")

    return [
        Organization.model_validate(organization).model_dump()
        for organization in organizations
    ]

@router.get("/by_activity/{activity_id}", response_model=list[Organization])
def get_organizations_by_activity_recursive(
    activity_id: int,
    max_depth: int = Query(3, ge=1, le=10, description="Максимальная глубина вложенности"),
    repo_factory: RepositoryFactory = Depends(get_repository_factory)
) -> list[dict[str, str]]:
    organizations = repo_factory.organization.get_multi_by_activity_recursive(
        activity_id=activity_id,
        max_depth=max_depth,
    )

    if not organizations:
        raise HTTPException(status_code=404, detail="Not found")

    return [
        Organization.model_validate(organization).model_dump()
        for organization in organizations
    ]
