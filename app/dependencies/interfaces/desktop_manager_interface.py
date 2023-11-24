class DesktopManagerInterface():
    
    def __init__(self):
        self._virtual_desktops_number: int
        self._os: str

        def get_virtual_desktops_number(self) -> int:
            """
            Get the number of total available virtual desktops
            """
            return self._virtual_desktops_count
        
        def get_os(self) -> str:
            return self._os

        def go_next_desktop(self) -> bool:
            pass

        def go_prev_desktop(self) -> bool:
            pass

        def go_desktop(self, desktop: int) -> bool:
            pass

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

        def go_bottom_desktop(dels) -> bool:
            pass
