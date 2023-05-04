from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Extra


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


class AmountPerTimeEnum(Enum):
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    YEAR = "year"


class Rate(BaseModel):
    amount: int
    amountPerTime: AmountPerTimeEnum


class CreateJob(BaseModel, extra=Extra.forbid):
    title: str
    rate: Rate
    benefits: Optional[str]
    location: UUID
    remoteAllowed: bool
    contractType: ContractTypeEnum
    description: str
    skills: list[UUID]
    liveUntil: datetime


class Location(BaseModel, extra=Extra.forbid):
    id: UUID
    city: str
    state: Optional[str]
    country: str


class Recruiter(BaseModel):
    id: UUID
    name: str


class GetJob(CreateJob):
    id: UUID
    dateListed: datetime
    location: Location
    recruiter: Recruiter
    skill: list[str]


class CreateApplication(BaseModel, extra=Extra.forbid):
    coverLetter: Optional[str]
    availability: datetime


class ApplicationCandidate(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str


class ApplicationStatusEnum(Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"


class GetApplicationForRecruiter(CreateApplication):
    id: UUID
    candidate: ApplicationCandidate
    status: ApplicationStatusEnum


class SkillsExperience(BaseModel):
    id: UUID
    yearsExperience: int


class RegisterCandidate(BaseModel, extra=Extra.forbid):
    name: str
    surname: str
    email: str
    phone: str
    location: UUID
    willingForRelocate: bool
    remoteOk: bool
    skills: list[SkillsExperience]
    currenTitle: str
    yearsExperience: int
    lookingFor: list[str]


class GetSkillsExperience(BaseModel):
    name: str
    yearsExperience: int


class GetCandidate(BaseModel, extra=Extra.forbid):
    id: UUID
    created: datetime
    name: str
    email: str
    phone: str
    location: Location
    willingForRelocate: bool
    remoteOk: bool
    skills: list[GetSkillsExperience]
    currenTitle: str
    yearsExperience: int
    lookingFor: list[str]


class Skills(BaseModel):
    id: UUID
    name: str


class ListSkills(BaseModel, extra=Extra.forbid):
    pages: int
    skills: list[Skills]


class ListLocations(BaseModel, extra=Extra.forbid):
    pages: int
    locations: list[Location]
