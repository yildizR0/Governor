import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

import asyncio, ast
import websockets
import serial, aioserial

aioserial_instance: aioserial.AioSerial = aioserial.AioSerial(port='/dev/tty.usbserial-2140', baudrate=115200)
#serial.Serial("/dev/tty.usbserial-2140", 115200, timeout=0.01)
# Function to receive messages from the server
async def receive_messages(websocket):
    #arduino = await serial_asyncio.connect(url="/dev/tty.usbserial-2140", baudrate=115200)
    async for message in websocket:
        data = ast.literal_eval(message)
        x = data[0]
        y = data[1]
        await aioserial_instance.write_async(f"{x},{y}\n".encode())
        await asyncio.sleep(0.02)
        #arduino.write(f"{message[1]},{message[0]}\n".encode())

# Function to handle the chat client
async def chat():
    async with websockets.connect('ws://localhost:12345') as websocket:
        await asyncio.gather(
            receive_messages(websocket)
        )

if __name__ == "__main__":
    asyncio.run(chat())