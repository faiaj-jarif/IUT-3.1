from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel

from database import create_db_and_tables, get_session
from models import User, Parcel, ParcelEvent


# --- Schemas ---

class UserCreate(BaseModel):
    name: str
    email: str

class ParcelCreate(BaseModel):
    tracking_number: str
    courier: str
    description: str
    recipient_id: int


# --- App Initialization ---

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Task E3
@app.get("/parcels/{parcel_id}", response_model=Parcel)
def get_parcel(parcel_id: int,
               session: Session = Depends(get_session)):
    
    parcel = session.get(Parcel, parcel_id)
    if not parcel:
        raise HTTPException(
            status_code=404, detail="Parcel not found")
    
    return parcel


# Task D1
@app.get("/parcels", response_model=list[Parcel])
def list_parcels(session: Session = Depends(get_session)):
    return session.exec(select(Parcel)).all()




# Task E1
@app.post("/users", response_model=User, status_code=201)
def create_user(data: UserCreate,
                session: Session = Depends(get_session)):
    
    user = User(name=data.name, email=data.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Task E2
@app.post("/parcels", response_model=Parcel, status_code=201)
def create_parcel(data: ParcelCreate,
                  session: Session = Depends(get_session)):

    recipient = session.get(User, data.recipient_id)
    if not recipient:
        raise HTTPException(
            status_code=404,
            detail="Recipient not found")
        
    existing_parcel = session.exec(
        select(Parcel).where(Parcel.tracking_number == data.tracking_number)
    ).first()

    if existing_parcel:
        raise HTTPException(
            status_code=409,
            detail="Tracking number already exists")

    parcel = Parcel(
        tracking_number=data.tracking_number,
        courier=data.courier,
        description=data.description,
        recipient_id=data.recipient_id,
        status="registered"
    )

    session.add(parcel)
    session.commit()
    session.refresh(parcel)
    return parcel



# Task E4
@app.put("/parcels/{parcel_id}", response_model=Parcel)
def update_parcel(parcel_id: int, data: ParcelCreate,
                  session: Session = Depends(get_session)):

    parcel = session.get(Parcel, parcel_id)
    if not parcel:
        raise HTTPException(
            status_code=404, detail="Parcel not found")
        
    recipient = session.get(User, data.recipient_id)
    if not recipient:
        raise HTTPException(
            status_code=404, detail="Recipient not found")
        
    existing_parcel = session.exec(
        select(Parcel).where(Parcel.tracking_number == data.tracking_number)
    ).first()

    if existing_parcel and existing_parcel.id != parcel.id:
        raise HTTPException(
            status_code=409, detail="Tracking number belongs to a different parcel")

    parcel.tracking_number = data.tracking_number
    parcel.courier = data.courier
    parcel.description = data.description
    parcel.recipient_id = data.recipient_id
    parcel.updated_at = datetime.now(timezone.utc)

    session.add(parcel)
    session.commit()
    session.refresh(parcel)
    return parcel


# Task E5
@app.delete("/parcels/{parcel_id}")
def delete_parcel(parcel_id: int, session: Session = Depends(get_session)):
    parcel = session.get(Parcel, parcel_id)
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")

    events = session.exec(
        select(ParcelEvent).where(ParcelEvent.parcel_id == parcel_id)
    ).all()
    
    if events:
        raise HTTPException(status_code=409, detail="Cannot delete parcel with event history")

    session.delete(parcel)
    session.commit()
    return {"message": "Parcel deleted"}