from fastapi import FastAPI, Depends
import models
from database import engine, Sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def create_database():
    return{"Database": "Created"}

def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def read_all(db:Session = Depends(get_db)):
    return db.query(models.Todos).all()



