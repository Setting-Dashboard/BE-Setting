from fastapi import FastAPI
from controllers.setting import router as SettingController
from db.mongodb import connect_to_mongo, close_mongo_connection

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.on_event("startup")
def startup():
    connect_to_mongo()

@app.on_event("shutdown")
def shutdown():
    close_mongo_connection()

app.include_router(SettingController)