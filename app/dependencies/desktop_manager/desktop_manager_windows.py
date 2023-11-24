from dependencies.interfaces.desktop_manager_interface import DesktopManagerInterface
from pyvda import VirtualDesktop, get_virtual_desktops

class DesktopManagerWindows(DesktopManagerInterface):
    def __init__(self):
        super.__init__()

        self._virtual_desktops_number = len(get_virtual_desktops())

    

    