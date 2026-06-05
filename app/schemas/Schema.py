from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class EventInXDM(BaseModel):
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str


class fullPayload(BaseModel):
    fullPayload: any


class EventOutXDM(BaseModel):
    eventType: str 
    pageURL: str
    timestamp: str
    pageName: str

