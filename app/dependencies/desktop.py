from app.utils.functions import get_desktop_environment
from app.dependencies.desktop_manager import DesktopManagerInterface, DesktopManagerGeneric, DesktopManagerWindows, DesktopManagerWMCtrl
from app.utils.exceptions import WMCtrlNotInstalled

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Desktop(metaclass=Singleton):
    __desktop_manager: DesktopManagerInterface
    __desktop_environment: str

    def __init__(self) -> None:
        self.__desktop_environment = get_desktop_environment()

        if self.__desktop_environment == 'windows':
            self.__desktop_manager = DesktopManagerWindows()
        elif(self.__desktop_environment in ["gnome","unity", "cinnamon", "mate", "xfce4", "lxde", "fluxbox", 
                                            "blackbox", "openbox", "icewm", "jwm", "afterstep","trinity", "kde"]):
            try:
                self.__desktop_manager = DesktopManagerWMCtrl()
            except WMCtrlNotInstalled as ex:
                print("wmctrl is not installed! Please install it!")

                print("Using generic desktop manager")
                self.__desktop_manager = DesktopManagerGeneric()
        else:
            self.__desktop_manager = DesktopManagerGeneric()
            
    def get_current_desktop(self) -> int:
        return self.__desktop_manager.get_current_desktop()
    
    def go_desktop(self, desktop: int) -> bool:
        return self.__desktop_manager.go_desktop(desktop)
    

    
