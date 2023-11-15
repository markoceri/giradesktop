from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from models import VirtualDesktopResponse, ElioDevice
from utils import desktop_environment

routes = APIRouter()

@routes.get("/virtualdesktop", response_model=VirtualDesktopResponse)
def get_virtual_desktop():
    return VirtualDesktopResponse(actual=desktop_environment.get_current_desktop())

@routes.post("/virtualdesktop")
async def set_virtual_desktop(request: Request):
    json_payload = await request.json()

    vd = int(json_payload['cubePosition'])
    print("Set desktop to:", vd)
    if desktop_environment.switch_to_desktop(vd):
        return VirtualDesktopResponse(actual=vd)
    else:
        JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)

async def print_request(request: Request):
    print(f'request header       : {dict(request.headers.items())}' )
    print(f'request query params : {dict(request.query_params.items())}')  
    try : 
        print(f'request json         : {await request.json()}')
    except Exception as err:
        # could not parse json
        print(f'request body         : {await request.body()}')