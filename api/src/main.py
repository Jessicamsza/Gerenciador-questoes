from .database import engine, Base
from .models import card_model
from .routers import card_router
from fastapi import FastAPI


Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="My API of personalized studysets",
    description="API to add personalize questions and get on demand quizes",
    version="0.1.0"
)

app.include_router(card_router.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "welcome to the personalized studysets API! "}