from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import crud
import schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"message": "Not found"}}
)


@router.get("/me/")
async def read_users_me(current_user: schemas.User = Depends(crud.get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: schemas.User = Depends(crud.get_current_active_user)):
    return [{"Item ID": "IT001", "Owner": current_user.username}]


@router.post("/me/create-items", response_model=schemas.Item)
def create_item_for_user(item: schemas.ItemCreate, current_user: schemas.User = Depends(crud.get_current_active_user),
                         db: Session = Depends(crud.get_db)):
    return crud.create_user_item(user_id=current_user.id, item=item, db=db)
