from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Any


class EventInXDM(BaseModel):
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str


class fullPayload(BaseModel):
    fullPayload: dict[str, Any]


class EventOutXDM(BaseModel):
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str

