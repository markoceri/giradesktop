from pyvda import VirtualDesktop, get_virtual_desktops

def switch_to_desktop(virtual_desktop: int = 1) -> bool:
    """
    Switch to selected virtual desktop
    """
    total_virtual_desktop: int

    total_virtual_desktop = get_total_virtual_desktops()

    if total_virtual_desktop > 0 and virtual_desktop >= 1 and virtual_desktop <= total_virtual_desktop:
        VirtualDesktop(virtual_desktop).go()

        return True
    else:
        return False
    
def get_current_desktop() -> int:
    """
    Get the current used virtual desktop
    """
    current_desktop = VirtualDesktop.current()

    if current_desktop:
        return current_desktop.number
    else:
        return 0

def get_total_virtual_desktops() -> int:
    """
    Get the number of total available virtual desktops
    """
    return len(get_virtual_desktops())