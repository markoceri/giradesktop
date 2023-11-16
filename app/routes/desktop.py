from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

from models import VirtualDesktopResponse, ElioDevice

from dependencies import desktop_environment

router = APIRouter(
    prefix="/desktop"
)

@router.get("/", response_model=VirtualDesktopResponse)
def get_desktop():
    return VirtualDesktopResponse(actual=desktop_environment.get_current_desktop())

@router.post("/")
async def set_desktop(request: Request):
    json_payload = await request.json()

    vd = int(json_payload['cubePosition'])
    print("Set desktop to:", vd)
    #if desktop_environment.switch_to_desktop(vd):
    return VirtualDesktopResponse(actual=vd)
    # else:
    #     JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)