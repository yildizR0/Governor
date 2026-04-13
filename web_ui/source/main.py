import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from nicegui import ui, page, app
#from picamera2 import Picamera2
from collections import deque
import serial, threading
from source import appstate
from source.view import v_joystick
from source.viewmodel import vm_joystick
import websockets, asyncio
connected_clients = set()
#from source.repository import r_joystick
#from source.services import bytes2disk

os.makedirs(os.path.join(os.getcwd() ,"frames"), exist_ok=True)

frame_buffer = deque(maxlen=500)
csv_buffer = deque(maxlen=500)
camera = None #Picamera2()
#camera.configure(camera.create_video_configuration({"size": (320, 240), "format": "RGB888"},controls={"FrameRate": 10}))
#camera.start()

state = appstate.AppState()
#b2d = bytes2disk.Bytes2Disk(frame_buffer, csv_buffer)
repo_joystick = None #r_joystick.JoystickRepo(arduino, camera, frame_buffer, csv_buffer)
viewmodel_joystick = vm_joystick.JoystickViewModel(repo_joystick, state, connected_clients)

async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print("Received from client:", message)
    except:
        pass
    finally:
        connected_clients.remove(websocket)

@app.on_startup
async def start_websocket_server():
    async with websockets.serve(handle_client, 'localhost', 12345):
        await asyncio.Future()

@ui.page('/steuern')    
def joystick_view():
    v_joystick.JoystickView(viewmodel_joystick)

#threading.Thread(target=b2d.save_frame, daemon=True).start()
#threading.Thread(target=b2d.save_csv, daemon=True).start()

ui.run(title="GovernorBOT WebUI", reload=False, show=False)
