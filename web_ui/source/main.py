import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from nicegui import ui
from source import appstate
from source.view import v_joystick
from source.viewmodel import vm_joystick
from source.repository import r_joystick
 
state = appstate.AppState()

repo_joystick = r_joystick.JoystickRepo()
viewmodel_joystick = vm_joystick.JoystickViewModel(repo_joystick, state)
view_joystick = v_joystick.JoystickView(viewmodel_joystick)

ui.run(title="GovernorBOT WebUI", reload=False, )