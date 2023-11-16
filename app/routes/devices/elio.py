from fastapi import APIRouter

from models import ElioDevice

router = APIRouter(
    prefix="/devices/elio"
)

@router.post("/")
async def catch_data_from_elio_device(device: ElioDevice):
    print(f'elio device       : {dict(device)}' )

    return device