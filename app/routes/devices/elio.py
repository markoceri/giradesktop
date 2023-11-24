from fastapi import APIRouter

from app.models import ElioDevice

router = APIRouter(
    prefix="/elio"
)

@router.post("/")
async def catch_data_from_elio_device(device: ElioDevice):
    print(f'elio device       : {dict(device)}' )

    return device