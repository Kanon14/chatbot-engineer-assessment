from fastapi import APIRouter, Query
from app.services.outlet_query import search_outlet_db

router = APIRouter()

@router.get("/")
async def search_outlet(location: str = Query(..., description="Outlet name, city, or keyword")):
    result = search_outlet_db(location)
    return {"location": location, "result": result}
