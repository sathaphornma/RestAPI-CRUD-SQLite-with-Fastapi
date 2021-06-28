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


@router.post("/me/create-items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):
    return crud.create_user_item(user_id=current_user.id, item=item, db=db)


@router.get("/me/items/")
async def read_items(current_user: schemas.User = Depends(crud.get_current_active_user),
                     db: Session = Depends(crud.get_db)):
    return crud.get_user_item(user_id=current_user.id, db=db)


@router.get("/me/items/{item_id}")
def read_item_id(item_id: int, current_user: schemas.User = Depends(crud.get_current_active_user),
                 db: Session = Depends(crud.get_db)):
    return crud.get_user_item_id(user_id=current_user.id, item_id=item_id, db=db)


@router.put("/me/items/{item_id}/{title}/{description}")
def update_item(item_id: int, title: str, description: str,
                current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):

    return crud.put_user_item_id(user_id=current_user.id,
                                 item_id=item_id,
                                 title=title,
                                 description=description,
                                 db=db)


@router.delete("/me/items/delete/{item_id}")
def delete_item(item_id: int, current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):
    return crud.delete_user_item(user_id=current_user.id, item_id=item_id, db=db)
