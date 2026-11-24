from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    role: str = "student"

class Parcel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tracking_number: str = Field(index=True, unique=True)
    courier: str
    description: str
    recipient_id: int = Field(foreign_key="user.id")
    status: str = "registered"
    pickup_code_hash: str | None = None
    code_expires_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ParcelEvent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    parcel_id: int = Field(foreign_key="parcel.id")
    actor_id: int = Field(foreign_key="user.id")
    event_type: str
    note: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))