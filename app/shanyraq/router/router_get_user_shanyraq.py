from typing import Any
from pydantic import Field
from fastapi import Depends, Response
from app.utils import AppModel
from app.auth.adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from app.auth.router.dependencies import parse_jwt_user_data


class GetSnanyraqResponse(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    room_count: int
    description: str
    user_id: Any


@router.get("/{shanyraq_id:str}", response_model=GetSnanyraqResponse)
def get_shanyraq(
    shanyraq_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyraq = svc.repository.get_shanyraq(shanyraq_id)
    if shanyraq is None:
        return Response(status_code=404)
    return GetSnanyraqResponse(**shanyraq)