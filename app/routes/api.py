from fastapi import APIRouter

from app.routes.devices import router as devices_router
from app.routes.desktop import router as desktop_router

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

# API devices routes
router.include_router(devices_router)

# API desktop routes
router.include_router(desktop_router)