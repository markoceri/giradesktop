from typing import Union
from pydantic import BaseModel


class VirtualDesktopResponse(BaseModel):
    """
    Response for virtual desktop data endpoint
    """

    actual: int

class ElioDevice(BaseModel):
    time: Union[int, None] = None
    plugged: Union[bool, None] = None
    wirelessCharging: Union[bool, None] = None
    sunDetected: Union[bool, None] = None
    batteryVoltage: Union[float, None] = None
    tempC: Union[float, None] = None
    tempF: Union[float, None] = None
    humidity: Union[float, None] = None
    tvoc: Union[float, None] = None
    proximity: Union[float, None] = None
    light: Union[float, None] = None
    lightRed: Union[int, None] = None
    lightGreen: Union[int, None] = None
    lightBlue: Union[int, None] = None
    IRlight: Union[int, None] = None
    cubePosition: Union[int, None] = None
    decahedronPosition: Union[int, None] = None
    pressure: Union[float, None] = None
    altitude: Union[float, None] = None
    tempOutC: Union[float, None] = None
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None
    D1: Union[bool, None] = None
    D2: Union[bool, None] = None
    D3: Union[bool, None] = None
    D4: Union[bool, None] = None
    D5: Union[bool, None] = None
    LED: Union[int, None] = None
    version: Union[str, None] = None
    MAC: Union[str, None] = None


