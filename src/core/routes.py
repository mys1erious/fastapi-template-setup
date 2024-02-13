from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    s = 's'
    return {"health_check": "OK"}
