from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import crud
import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"message": "Not found"}}
)


@router.get("/info")
async def read_users_me(current_user: schemas.User = Depends(crud.get_current_active_user)):
    return current_user
