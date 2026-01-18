from nicegui import ui

class JoystickView():
    def __init__(self, vm):
        super().__init__()
        self.vm = vm
        self.initiate_ui()

    def initiate_ui(self):
        with ui.column().classes("justify-center"):
            ui.joystick(
                    color='blue', size=100, **{"mode": "static"},
                    on_move=lambda e: self.vm.coordinates(f'{e.x:.3f}', f'{e.y:.3f}'),
                    on_end=lambda _: self.vm.coordinates(f'0', f'0'),
                ).classes('bg-slate-300')