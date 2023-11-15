from pydantic import BaseModel


class VirtualDesktopResponse(BaseModel):
    """
    Response for virtual desktop data endpoint
    """

    actual: int

class ElioDevice(BaseModel):
    time: int
    plugged: bool
    wirelessCharging: bool
    sunDetected: bool
    batteryVoltage: float
    tempC: float
    tempF: float
    humidity: float
    tvoc: float
    proximity: float
    light: float
    lightRed: int
    lightGreen: int
    lightBlue: int
    IRlight: int
    cubePosition: int
    decahedronPosition: int
    pressure: float
    altitude: float
    tempOutC: float
    latitude: float
    longitude: float
    D1: bool
    D2: bool
    D3: bool
    D4: bool
    D5: bool
    LED: int
    version: str
    MAC: str


