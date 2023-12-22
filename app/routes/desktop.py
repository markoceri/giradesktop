from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

from app.models import DesktopResponse
from app.dependencies.desktop import Desktop

router = APIRouter(
    prefix="/desktop",
    tags=["desktop"]
)

desktop: Desktop = Desktop()

@router.get("/", response_model=DesktopResponse)
def get_desktop():
    return DesktopResponse(active=desktop.get_current_desktop())

@router.post("/")
async def go_to_desktop(desktopId: int):
    if desktop.go_desktop(desktopId):
        return DesktopResponse(active=desktopId)
    else:
        JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)