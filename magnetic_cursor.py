import serial
import pyautogui
import time

# -----------------------------
# Serial Port Configuration
# -----------------------------
SERIAL_PORT = "COM3"      # Change this to your ESP32 COM port
BAUD_RATE = 115200

# -----------------------------
# Cursor Movement Settings
# -----------------------------
MOVE_DISTANCE = 30

# -----------------------------
# Connect to ESP32
# -----------------------------
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)

print("Magnetic Cursor Control Started...")

while True:

    if ser.in_waiting:

        line = ser.readline().decode('utf-8').strip()

        print(line)

        # Detect sensor triggers
        if "MAGNET DETECTED on GPIO" in line:

            # Extract GPIO number
            gpio = int(line.split()[-1])

            # -----------------------------
            # Cursor Controls
            # -----------------------------

            # LEFT
            if gpio == 32:
                pyautogui.moveRel(-MOVE_DISTANCE, 0)

            # RIGHT
            elif gpio == 33:
                pyautogui.moveRel(MOVE_DISTANCE, 0)

            # UP
            elif gpio == 25:
                pyautogui.moveRel(0, -MOVE_DISTANCE)

            # RIGHT CLICK
            elif gpio == 26:
                pyautogui.rightClick()

            # DOWN
            elif gpio == 27:
                pyautogui.moveRel(0, MOVE_DISTANCE)

            time.sleep(0.15)
