from datetime import date
from enum import Enum
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Query, Depends
from pydantic import BaseModel
from starlette import status

router = APIRouter()


class SortEnum(Enum):
    ASC = "asc"
    DESC = "desc"


class Pagination(BaseModel):
    perPage: int
    page: int
    order: SortEnum


class CandidateStatusEnum(Enum):
    ACTIVELY_LOOKING = "activelyLooking"
    NOT_LOOKING = "notLooking"
    NOT_LOOKING_BUT_INTERESTED = "notLookingButInterested"


class JobsSortByEnum(Enum):
    DATE_POSTED = "datePosted"
    RATE = "rate"


class ContractTypeEnum(Enum):
    PERMANENT = "permanent"
    CONTRACT = "contract"


def pagination_params(
    page: int = Query(ge=1, required=False, default=1),
    perPage: int = Query(ge=1, le=100, required=False, default=1),
    order: SortEnum = SortEnum.DESC,
):
    return Pagination(perPage=perPage, page=page, order=order.value)


@router.get("/skills")
def list_skills(pagination: Annotated[Pagination, Depends(pagination_params)]):
    pass


@router.get("/locations")
def list_locations(pagination: Annotated[Pagination, Depends(pagination_params)]):
    pass


@router.get("/jobs")
def list_jobs(
    pagination: Annotated[Pagination, Depends(pagination_params)],
    sortBy: JobsSortByEnum | None = None,
    contractType: ContractTypeEnum | None = None,
    dateSincePosted: date | None = None,
    minimumInclusiveRare: int | None = None,
    keyword: str | None = None,
    location: UUID | None = None,
    skills: UUID | None = None,
):
    pass


@router.post("/jobs", status_code=status.HTTP_201_CREATED)
def create_job():
    pass


@router.get("/jobs/{id}")
def get_job(id: UUID):
    pass


@router.put("jobs/{id}")
def update_job(id: UUID):
    pass


@router.post("/jobs/{id}/apply", status_code=status.HTTP_201_CREATED)
def apply_for_job(id: UUID):
    pass


@router.get("/jobs/{id}/applications")
def list_job_application_recruiter(id: UUID):
    pass


@router.get("/applications")
def list_applications_candidate(
    pagination: Annotated[Pagination, Depends(pagination_params)]
):
    pass


@router.get("/applications/{id}")
def get_application_for_candidate(id: UUID):
    pass


@router.post("/applications/{id}/cancel", status_code=status.HTTP_201_CREATED)
def cancel_application(id: UUID):
    pass


@router.get("/candidates")
def list_candidates(
    perPage: int = Query(default=10, ge=1),
    page: int = Query(default=1, ge=1),
    status: CandidateStatusEnum | None = None,
    skills: UUID | None = None,
    experience: int | None = None,
    location: UUID | None = None,
    willingToRelocate: bool | None = None,
    remoteOK: bool | None = None,
):
    pass


@router.post("/candidates", status_code=status.HTTP_201_CREATED)
def register_candidate():
    pass


@router.get("/candidates/{id}")
def get_candidate(id: UUID):
    pass


@router.put("/candidates/{id}")
def update_candidate(id: UUID):
    pass


@router.delete("/candidates/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidate(id: UUID):
    pass


@router.get("/candidates/{id}/cv")
def download_cv(id: UUID):
    pass


@router.put("/candidates/{id}/cv")
def upload_cv(id: UUID):
    pass


@router.get("/recruiters")
def get_recruinters():
    pass


@router.post("/recruiters", status_code=status.HTTP_201_CREATED)
def register_recruiter():
    pass


@router.get("/recruiters/{id}")
def get_recruiter(id: UUID):
    pass


@router.put("/recruiters/{id}")
def update_recruiter(id: UUID):
    pass


@router.delete("/recruiters/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recruiter(id: UUID):
    pass
