from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, Any


class EventInXDM(BaseModel):
    xdm: dict[str,Any]
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str
    source: str


class fullPayload(BaseModel):
    fullPayload: dict[str, Any]


class EventOutXDM(BaseModel):
    xdm: dict[str,Any]
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str
    source: str

