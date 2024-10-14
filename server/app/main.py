import uvicorn
from fastapi import FastAPI

from app.api.routers.bookings import router as bookings_router
from app.models import Base
from app.database import get_db_session

app = FastAPI()


# create database
@app.on_event("startup")
def init_tables():
    with get_db_session() as sess:
        conn = sess.connection()
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
        sess.commit()
        sess.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Routers
app.include_router(bookings_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
