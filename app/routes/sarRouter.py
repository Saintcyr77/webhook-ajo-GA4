from fastapi import HTTPException, APIRouter, status
from app.Storage.testStore import obj
from app.schemas.Schema import EventOutXDM, EventInXDM, fullPayload

router = APIRouter(prefix='/api/v1/events', tags=['events'])

@router.get('/',response_model=list[EventOutXDM])
def getAllEvents():
    data = obj.getData()

    if len(data)==0:
           return {
        "eventType": "dummy",
        "pageURL": "/dummy",
        "timestamp": "2026-06-07",
        "pageName": "Home"
    }

    return data


@router.post('/EventIn',response_model=EventOutXDM,status_code=status.HTTP_201_CREATED)

def getEvents(payload:EventInXDM):
      data = obj.getData()

      newData = {
            "eventType": payload.eventType,
            "pageURL": payload.pageURL,
            "timestamp": payload.timestamp,
            "pageName": payload.pageName
      }
      data.append(newData)
      obj.loadData(data)
      return newData      