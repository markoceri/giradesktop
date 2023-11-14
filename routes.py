from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from models import VirtualDesktopResponse
from utils import desktop_environment

routes = APIRouter()

@routes.get("/virtualdesktop", response_model=VirtualDesktopResponse)
def get_virtual_desktop():
    return VirtualDesktopResponse(actual=desktop_environment.get_current_desktop())


@routes.post("/virtualdesktop", response_model=VirtualDesktopResponse)
def set_virtual_desktop(vd: int):
    if desktop_environment.switch_to_desktop(vd):
        return VirtualDesktopResponse(actual=vd)
    else:
        JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)