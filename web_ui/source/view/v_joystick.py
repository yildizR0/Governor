from nicegui import ui

class JoystickView():
    def __init__(self, vm):
        super().__init__()
        self.vm = vm
        self.initiate_ui()

    def initiate_ui(self):
        with ui.row().classes("w-full h-screen items-center justify-center bg-slate-100"):
            with ui.card().classes("p-6 rounded-2xl shadow-lg bg-white"):
                ui.label("GovernorNET 6.7GHz").classes("text-lg font-semibold mb-4 text-center")
                ui.joystick(
                    color='blue',
                    size=120,
                    **{"mode": "static"},
                    on_move=lambda e: self.vm.coordinates(f'{e.x:.3f}', f'{e.y:.3f}'),
                    on_end=lambda _: self.vm.coordinates('0', '0'),
                ).classes("bg-slate-200 rounded-full")