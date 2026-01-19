from nicegui import ui

class JoystickView():
    def __init__(self, vm):
        super().__init__()
        self.vm = vm
        # Wir speichern die aktuellen Werte zwischen
        self.current_x = "0.000"
        self.current_y = "0.000"
        # Ein Timer, der standardmäßig nicht läuft (active=False)
        self.update_timer = ui.timer(0.01, self.send_coordinates, active=False)
        self.initiate_ui()

    def send_coordinates(self):
        """Wird vom Timer aufgerufen"""
        self.vm.coordinates(self.current_x, self.current_y)

    def handle_move(self, e):
        """Aktualisiert nur die internen Werte"""
        self.current_x = f'{e.x:.3f}'
        self.current_y = f'{e.y:.3f}'
        # Falls der Timer noch nicht läuft, starte ihn (Sicherheitsnetz)
        self.update_timer.activate()

    def handle_end(self):
        """Stoppt den Loop und setzt auf Null zurück"""
        self.update_timer.deactivate()
        self.current_x = "0"
        self.current_y = "0"
        self.vm.coordinates('0', '0')

    def initiate_ui(self):
        with ui.row().classes("w-full h-screen items-center justify-center bg-slate-100"):
            with ui.card().classes("p-6 rounded-2xl shadow-lg bg-white"):
                ui.label("GovernorNET 6.7GHz").classes("text-lg font-semibold mb-4 text-center")
                ui.joystick(
                    color='blue',
                    size=120,
                    **{"mode": "static"},
                    on_move=self.handle_move,
                    on_end=lambda _: self.handle_end(),
                ).classes("bg-slate-200 rounded-full")