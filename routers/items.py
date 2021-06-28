from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from Core import schemas, crud

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"message": "Not found"}}
)


@router.post("/create", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):
    return crud.create_user_item(user_id=current_user.id, item=item, db=db)


@router.get("/get_all")
async def read_items(current_user: schemas.User = Depends(crud.get_current_active_user),
                     db: Session = Depends(crud.get_db)):
    return crud.get_user_item(user_id=current_user.id, db=db)


@router.get("/get_id/{item_id}")
def read_item_id(item_id: int, current_user: schemas.User = Depends(crud.get_current_active_user),
                 db: Session = Depends(crud.get_db)):
    return crud.get_user_item_id(user_id=current_user.id, item_id=item_id, db=db)


@router.put("/update/{item_id}/{title}/{description}")
def update_item(item_id: int, title: str, description: str,
                current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):
    return crud.put_user_item_id(user_id=current_user.id,
                                 item_id=item_id,
                                 title=title,
                                 description=description,
                                 db=db)


@router.delete("/delete/{item_id}")
def delete_item(item_id: int, current_user: schemas.User = Depends(crud.get_current_active_user),
                db: Session = Depends(crud.get_db)):
    return crud.delete_user_item(user_id=current_user.id, item_id=item_id, db=db)
