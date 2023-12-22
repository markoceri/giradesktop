from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.dependencies.desktop import Desktop
from app.models import ElioDevice, DesktopResponse

router = APIRouter(
    prefix="/elio"
)

desktop: Desktop = Desktop()

@router.post("")
async def catch_data_from_elio_device(device: ElioDevice):
    print(f'elio device       : {dict(device)}' )
    print(f'position          : {device.cubePosition}' )
    
    if desktop.go_desktop(device.cubePosition):
        return DesktopResponse(active=device.cubePosition)
    else:
        JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)

    return device