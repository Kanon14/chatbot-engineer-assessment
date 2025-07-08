from fastapi import FastAPI
from app.routes import product, outlet

app = FastAPI(title="ZUS Coffee Chatbot API")

# Register routes
app.include_router(product.router, prefix="/products", tags=["Product"])
app.include_router(outlet.router, prefix="/outlets", tags=["Outlet"])
