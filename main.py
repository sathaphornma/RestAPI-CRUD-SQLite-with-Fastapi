from fastapi import FastAPI
from Routers import default, users, items

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app = FastAPI(
    title="Python RestAPI with FastAPI.",
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

app.include_router(default.router)
app.include_router(users.router)
app.include_router(items.router)
