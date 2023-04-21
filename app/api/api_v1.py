from fastapi import APIRouter

# Import your endpoint routers
from app.api.endpoints import users, templates, payments

api_router = APIRouter()

# Register your endpoint routers
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(templates.router, prefix="/templates", tags=["templates"])
api_router.include_router(payments.router, prefix="/payments", tags=["payments"])
