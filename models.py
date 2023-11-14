from pydantic import BaseModel


class VirtualDesktopResponse(BaseModel):
    """
    Response for virtual desktop data endpoint
    """

    actual: int