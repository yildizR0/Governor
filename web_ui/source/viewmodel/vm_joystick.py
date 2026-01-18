import time

class JoystickViewModel():
    def __init__(self, repo, appstate):
        super().__init__()
        self.appstate = appstate
        self.repo = repo

    def coordinates(self, x, y):
        self.repo.serial_write(str(1500+(round(float(y)*-450))), str(1500+(round(float(x)*500))), float(y), float(x))
        time.sleep(0.01)

