from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/leads", response_model=List[schemas.LeadRead])
def read_leads(db: Session = Depends(get_db)):
    return db.query(models.Lead).all()


@app.post("/leads", response_model=schemas.LeadRead, status_code=201)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    db_lead = models.Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead


@app.patch("/leads/{lead_id}", response_model=schemas.LeadRead)
def update_lead(lead_id: int, lead_update: schemas.LeadUpdate, db: Session = Depends(get_db)):
    db_lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    for field, value in lead_update.dict(exclude_unset=True).items():
        setattr(db_lead, field, value)
    db.commit()
    db.refresh(db_lead)
    return db_lead
