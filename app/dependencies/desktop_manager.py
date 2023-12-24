import abc
import pyautogui

from app.utils.functions import get_desktop_environment
from app.utils.exceptions import WMCtrlNotInstalled

import sys, os

if sys.platform == 'linux':
    from wmctrl import Desktop
elif sys.platform == 'win32':
    from pyvda import VirtualDesktop, get_virtual_desktops

class DesktopManagerInterface(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__virtual_desktops_number: int

    def get_virtual_desktops_number(self) -> int:
        """
        Get the number of total available virtual desktops
        """
        return self.__virtual_desktops_number
    
    def set_virtual_desktops_number(self, dekstops) -> None:
        """
        Set the number of total available virtual desktops
        """
        self.__virtual_desktops_number = dekstops
    
    def go_next_desktop(self) -> bool:
        """
        Go to the next virtual desktop
        """
        return self.go_desktop(self.get_current_desktop() + 1 % (self.get_virtual_desktops_number()))

    def go_prev_desktop(self) -> bool:
        """
        Go to the previous virtual desktop
        """
        return self.go_desktop((self.get_virtual_desktops_number() if self.get_current_desktop() == 0 else self.get_current_desktop()) - 1 % (self.get_virtual_desktops_number()))

    @abc.abstractmethod
    def get_current_desktop(self) -> int:
        """
        Get the current used virtual desktop
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def go_desktop(self, desktop: int) -> bool:
        """
        Go to the specified virtual desktop face
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_right_desktop(self) -> bool:
        """
        Go to the virtual desktop on right face
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_left_desktop(self) -> bool:
        """
        Go to the virtual desktop on left face
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_up_desktop(self) -> bool:
        """
        Go to the virtual desktop on up face
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_down_desktop(self) -> bool:
        """
        Go to the virtual desktop on down face 
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_top_desktop(self) -> bool:
        """
        Go to the virtual desktop on top face
        """
        raise NotImplementedError

    @abc.abstractmethod
    def go_bottom_desktop(self) -> bool:
        """
        Go to the virtual desktop on bottom face
        """
        raise NotImplementedError

class DesktopManagerWindows(DesktopManagerInterface):        
    
    def __init__(self):
        super().__init__()

        self.set_virtual_desktops_number(len(get_virtual_desktops()))

    def get_current_desktop(self) -> int:
        current_desktop = VirtualDesktop.current()
        if current_desktop:
            return current_desktop.number - 1
        else:
            return -1

    def go_desktop(self, desktop: int) -> bool:
        if desktop >= 0 and  desktop < self.get_virtual_desktops_number():
            VirtualDesktop(desktop + 1).go()

            return True
        else:
            return False
        
    def go_right_desktop(self) -> bool:
        return self.go_next_desktop()

    def go_left_desktop(self) -> bool:
        return self.go_prev_desktop()
    
    def go_up_desktop(self) -> bool:
        return self.go_next_desktop()

    def go_down_desktop(self) -> bool:
        return self.go_prev_desktop()
    
    def go_top_desktop(self) -> bool:
        return self.go_desktop(self.get_virtual_desktops_number() - 1)
    
    def go_bottom_desktop(self) -> bool:
        return self.go_desktop(0)

class DesktopManagerWMCtrl(DesktopManagerInterface):    
    def __init__(self):
        super().__init__()

        try:
            self._virtual_desktops_number = Desktop.list()
        except:
            raise WMCtrlNotInstalled()
        
    def __system(self, s):
        return os.system(s)
        
    def get_current_desktop(self) -> int:
        active_desktop: Desktop

        active_desktop = Desktop.get_active()
        if active_desktop:
            return active_desktop.num
        else:
            return -1

    def set_virtual_desktops_number(self, dekstops) -> None:
        pass

    def go_next_desktop(self) -> bool:
        current_desktop: object
        actual_virtual_desktop: int
        next_virtual_desktop: int

        current_desktop = VirtualDesktop.current()
        if current_desktop:
            actual_virtual_desktop = current_desktop.number
        else:
            return False

        if actual_virtual_desktop < self._virtual_desktops_number:
            next_virtual_desktop = actual_virtual_desktop + 1
            self.go_desktop(next_virtual_desktop)

            return True
        else:
            return False
        
    def go_prev_desktop(self) -> bool:
        current_desktop: object
        actual_virtual_desktop: int
        prev_virtual_desktop: int

        current_desktop = VirtualDesktop.current()
        if current_desktop:
            actual_virtual_desktop = current_desktop.number
        else:
            return False

        if actual_virtual_desktop > 0:
            prev_virtual_desktop = actual_virtual_desktop - 1
            self.go_desktop(prev_virtual_desktop)

            return True
        else:
            return False

    def go_desktop(self, desktop: int) -> bool:
        if self.__system(f'wmctrl -s {desktop}'):
            return True
        else:
            return False
        
    def go_right_desktop(self) -> bool:
        return self.go_next_desktop()

    def go_left_desktop(self) -> bool:
        return self.go_prev_desktop()
    
    def go_up_desktop(self) -> bool:
        return self.go_next_desktop()

    def go_down_desktop(self) -> bool:
        return self.go_prev_desktop()
    
    def go_top_desktop(self) -> bool:
        return self.go_up_desktop(self.get_virtual_desktops_number())
    
    def go_bottom_desktop(self) -> bool:
        return self.go_up_desktop(0)

class DesktopManagerGeneric(DesktopManagerInterface):
    def __init__(self, base_desktop_key = 'f', additional_desktop_keys = ['ctrl']):
        super().__init__()

        self.__additional_desktop_keys: list
        self.__base_desktop_key: str

        self._virtual_desktops_number = 0
        self.__additional_desktop_keys = additional_desktop_keys
        self.__base_desktop_key = base_desktop_key

    def get_current_desktop(self) -> int:
        return -1

    def go_next_desktop(self) -> bool:
        pass
        
    def go_prev_desktop(self) -> bool:
        pass

    def go_desktop(self, desktop: int) -> bool:
        self._select_desktop_using_keyboard(desktop)

        return True
        
    def go_right_desktop(self) -> bool:
        pass

    def go_left_desktop(self) -> bool:
        pass
    
    def go_up_desktop(self) -> bool:
        pass

    def go_down_desktop(self) -> bool:
        pass
    
    def go_top_desktop(self) -> bool:
        pass
    
    def go_bottom_desktop(self) -> bool:
        pass
    
    def set_virtual_desktops_number(self, dekstops) -> None:
        self._virtual_desktops_number = dekstops

    def _select_desktop_with_additional_and_base_keys(self, desktop: int, base_key: str = '', additional_keys: list = []) -> None:
        key: str
        desktop_keys: list

        if base_key == '':
            return
        
        key = str.format('{0}{1}', base_key, desktop)
        desktop_keys = [*additional_keys, key]

        pyautogui.hotkey(*desktop_keys)

    def _select_desktop_using_keyboard(self, desktop: int) -> None:
        self._select_desktop_with_additional_and_base_keys(desktop, self.__base_desktop_key, self.__additional_desktop_keys)