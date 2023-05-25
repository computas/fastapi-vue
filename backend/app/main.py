
# IMPORTANT: implement the comments made by Luky

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Too allow all origins when frontend connects to backend
from pymongo import MongoClient
from .routers.people_routes import router as people_router

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb", 27017)
    app.database = app.mongodb_client["testing"]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(people_router, tags=["people"], prefix="/people")