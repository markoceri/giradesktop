from app.dependencies.interfaces.desktop_manager_interface import DesktopManagerInterface
from app.dependencies.desktop_manager.desktop_manager_windows import DesktopManagerWindows
from app.dependencies.desktop_manager import DesktopManagerGeneric

desktop_manager: DesktopManagerInterface

desktop_manager = DesktopManagerGeneric()

desktop_manager.go_desktop(3)