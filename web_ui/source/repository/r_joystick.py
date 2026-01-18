import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

import os
import uuid

class JoystickRepo():
    def __init__(self, arduino, camera, framebuffer, csvbuffer):
        super().__init__()
        self.arduino = arduino
        self.camera = camera
        self.frame_buffer = framebuffer
        self.csv_buffer = csvbuffer
        self.frame_id = 0
        self.frame_uuid = uuid.uuid1()

    def serial_write(self, y, x, rawy, rawx):
        self.arduino.write(f"{y},{x}\n".encode())
        filename = f"frames/{self.frame_uuid}_frame_{self.frame_id:04d}.jpg"
        self.frame_buffer.append((filename, self.camera.capture_array()))
        self.csv_buffer.append((filename, rawy, rawx))
        self.frame_id += 1


