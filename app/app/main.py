from fastapi import FastAPI
from .db.base import database
from .endpoints import commercials, post_data, housing_complexes, houses
import uvicorn

app = FastAPI(
    title="hackathon",
    description="API для хакатона",
    contact={
        "name": "Полодашвили Иосиф",
        "url": "https://t.me/Iosif_Polodashvili",
        "email": "iosif.polodashvili@mail.ru",
    },
    docs_url="/api/docs",
)


app.include_router(housing_complexes.router, prefix="/api/complexes", tags=["complexes"])
app.include_router(houses.router, prefix="/api/houses", tags=["houses"])
app.include_router(commercials.router, prefix="/api/commercials", tags=["commercials"])
app.include_router(post_data.router, prefix="/api/post_data", tags=["post_data"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
