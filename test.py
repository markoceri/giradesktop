from wmctrl import Window, Desktop

wins = Window.list()
desktop = Desktop.list()

test = Desktop.get_active()

desktop[3].active = True

asd = 0