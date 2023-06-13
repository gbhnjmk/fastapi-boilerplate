from fastapi import Depends, status
from typing import Any
from pydantic import Field
from app.utils import AppModel
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from ..service import Service, get_service
from . import router


class CreateSnanyraqRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    room_count: int
    description: str


class CreateSnanyraqResponse(AppModel):
    id: Any = Field(alias="_id")


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CreateSnanyraqResponse
)
def create_shanyraq(
    input: CreateSnanyraqRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyraq_id = svc.repository.create_shanyraq(jwt_data.user_id, input.dict())
    return CreateSnanyraqResponse(id=shanyraq_id)