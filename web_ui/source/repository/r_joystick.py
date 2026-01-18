from picamera2 import Picamera2
import os, random, threading, cv2, time, csv, serial
from collections import deque

class JoystickRepo():
    def __init__(self):
        super().__init__()
        os.makedirs(os.path.join(os.getcwd() ,"frames"), exist_ok=True)
        self.device = serial.Serial("/dev/ttyUSB1", 115200, timeout=0.01)
        self.initiate_camera()
        self.initate_csv()
        self.frame_id = 0
        self.buffers = deque(maxlen=500)

    def initiate_camera(self):
        self.camera = Picamera2()
        config = self.camera.create_video_configuration(
            {"size": (320, 240), "format": "RGB888"},
            controls={"FrameRate": 21}
        )
        self.camera.configure(config)
        self.camera.start()

    def initate_csv(self):
        csv_file = open("data.csv", "w", newline="")
        self.writer = csv.writer(csv_file)
        self.writer.writerow(["filename", "y", "x"])

    def bytes2disk(self):
        while True:
            while self.buffers:
                filename, frame = self.buffers.popleft()
                cv2.imwrite(filename, frame)

    def serial_write(self, y,x, rawy, rawx):
        self.device.write(f"{y},{x}\n".encode())
        filename = f"frames/frame_{self.frame_id:04d}.jpg"
        self.writer.writerow([filename, rawy, rawx])
        frame = self.camera.capture_array()
        self.buffers.append((filename, frame))
        frame_id += 1


