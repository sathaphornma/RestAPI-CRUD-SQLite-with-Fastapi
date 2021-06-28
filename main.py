from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud
import schemas
from routers import users

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app = FastAPI(
    title="Authentication with FastAPI.",
    description="This is mini project for create RestAPI, So I will create authentication with fastapi. This project "
                "using sqlite for database.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(crud.get_db)):
    user = crud.authenticate_user(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password is incorrect. Please try again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/sign-up/", response_model=schemas.User)
def sign_up(user: schemas.UserInDB, db: Session = Depends(crud.get_db)):
    # print(user)
    q_email, q_username = crud.check_user(db, email=user.email, username=user.username)
    # print(q_email, q_username)
    if q_email:
        raise HTTPException(status_code=400, detail="Email already exists.")
    elif q_username:
        raise HTTPException(status_code=400, detail="Username already exists.")
    else:
        crud.create_user(db=db, user=user)
        raise HTTPException(status_code=200, detail="Sign Up Success.")
