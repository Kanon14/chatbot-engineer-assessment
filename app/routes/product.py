from fastapi import APIRouter, Query
from app.services.product_query import query_product_vectorstore

router = APIRouter()

@router.get("/")
async def search_product(query: str = Query(..., description="Search product info")):
    result = query_product_vectorstore(query)
    return {"query": query, "response": result}
