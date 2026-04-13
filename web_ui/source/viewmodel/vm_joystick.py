import time, websockets

class JoystickViewModel():
    def __init__(self, repo, appstate, con_clients):
        super().__init__()
        self.appstate = appstate
        self.repo = repo
        self.connected_clients = con_clients

    async def coordinates(self, x, y):
        try:
            for client in self.connected_clients.copy():
                try:
                    await client.send(f"{str(1500+(round(float(y)*-450))), str(1500+(round(float(x)*500)))}")
                except websockets.exceptions.ConnectionClosed:
                    self.connected_clients.remove(client)
        except Exception as e:
            print(e)

