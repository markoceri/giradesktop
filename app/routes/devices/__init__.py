from fastapi import APIRouter

from app.routes.devices.elio import router as elio_router

router = APIRouter(
    prefix="/devices",
    tags=["devices"]
)

# All devices routes
router.include_router(elio_router)