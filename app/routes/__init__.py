from fastapi import APIRouter

from app.routes.api import router as api_routes

router = APIRouter()

# All devices routes
router.include_router(api_routes)