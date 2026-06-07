from fastapi import FastAPI
from app.routes.sarRouter import router as eventRouter
app = FastAPI()

app.include_router(eventRouter)
