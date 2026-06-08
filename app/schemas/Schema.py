from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Any
from sqlalchemy import Column, Integer, String
from app.Storage.DB import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    xdm = Column(String)
    event_type = Column(String, index=True)
    timestamp = (Column(String, index=True),)
    pageURL = Column(String)
    pageName = Column(String)
    source = Column(String)


class EventInXDM(BaseModel):
    xdm: dict[str, Any]
    eventType: str
    pageURL: str
    timestamp: str
    pageName: str
    source: str


class fullPayload(BaseModel):
    fullPayload: dict[str, Any]


class EventOutXDM(BaseModel):
    xdm: dict[str, Any]
    eventType: str
    pageURL: str
    timestamp: str
    pageName: str
    source: str
