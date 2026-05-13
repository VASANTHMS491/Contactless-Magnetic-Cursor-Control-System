<div align="center">

# 🧲 Contactless Magnetic Cursor Control System

### Real-Time Contactless Cursor Control via Hall Effect Sensors & ESP32

[![ESP32](https://img.shields.io/badge/ESP32-Dev%20Module-blue?style=flat-square&logo=espressif)](https://www.espressif.com/)
[![Arduino](https://img.shields.io/badge/Arduino-IDE-00979D?style=flat-square&logo=arduino)](https://www.arduino.cc/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

*Powered by magnetic field sensing and Python-based mouse control — no physical touch required.*

</div>

---

## 📖 Description

A contactless cursor control system that uses five **digital Hall effect sensors (49E-type)** to detect the presence of a small permanent magnet. As the magnet moves over each sensor, the corresponding digital pin goes HIGH or LOW, allowing the system to determine which action to perform.

The ESP32 reads digital values from all five sensors and transmits the data to a computer via **serial communication**. A Python script interprets this data and controls the mouse using `pyautogui` — four sensors handle cursor movement and one is dedicated to right-click.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧲 **Contactless Control** | No physical touch required for cursor movement |
| 📡 **Real-Time Detection** | Instant response to magnet position changes |
| 🎯 **Direction Mapping** | Four sensors detect cursor movement in four directions |
| 🖱️ **Cursor & Right-Click** | Python script moves the cursor and triggers right-click via a dedicated sensor |
| 💰 **Low Cost & Scalable** | Built with affordable, off-the-shelf components |
| ⚡ **Continuous Detection** | Detects movement instantly — no manual input needed |
| 🔧 **Easy Implementation** | No complex hardware protocols required |

---

## 🔧 Hardware Components

### 1. ESP32
Reads digital values from all five Hall effect sensors via GPIO pins, determines which sensor is triggered, and transmits the result to the PC via serial communication.

### 2. Digital Hall Effect Sensors — 49E-type (× 5)
Detect the presence of a magnetic field and output a digital HIGH or LOW signal. Four sensors handle cursor movement; one is dedicated to mouse right-click.

### 3. Neodymium Magnet
Acts as the primary input device. Hovering or moving the magnet over a sensor triggers the corresponding action.

### 4. Breadboard & Jumper Wires
Used for prototyping the sensor array and all component connections.

---

## 💻 Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software)
- Python 3.x
- Required Python libraries:

```bash
pip install pyserial pyautogui
```

| Library | Purpose |
|---|---|
| `pyserial` | Reads serial data from the ESP32 |
| `pyautogui` | Moves the cursor and triggers mouse clicks |

---

## 🔌 Pin Connections

All five Hall effect sensors output a **digital signal** read directly by ESP32 GPIO pins.

```cpp
int pins[5] = {32, 33, 25, 26, 27};
// GPIO26 → Right-click
// Remaining four pins → Cursor movement
```

| Sensor | Role | GPIO Pin |
|---|---|:---:|
| Hall Sensor 1 | Cursor Movement | GPIO32 |
| Hall Sensor 2 | Cursor Movement | GPIO33 |
| Hall Sensor 3 | Cursor Movement | GPIO25 |
| Hall Sensor 4 | **Right-Click** 🖱️ | GPIO26 |
| Hall Sensor 5 | Cursor Movement | GPIO27 |
| ESP32 VIN | Power | 5V Supply |
| ESP32 GND | Ground | Common GND |

> All sensor VCC pins connect to **3.3V** on the ESP32. All GND pins share a **common ground**.

### Wiring Diagram

```
  +-------------------+   +-------------------+   +-------------------+
  |   Hall Sensor 1   |   |   Hall Sensor 2   |   |   Hall Sensor 3   |
  |  (Cursor Move)    |   |  (Cursor Move)    |   |  (Cursor Move)    |
  |                   |   |                   |   |                   |
  |  VCC ── 3.3V      |   |  VCC ── 3.3V      |   |  VCC ── 3.3V      |
  |  GND ── GND       |   |  GND ── GND       |   |  GND ── GND       |
  |  DOUT── GPIO32    |   |  DOUT── GPIO33    |   |  DOUT── GPIO25    |
  +-------------------+   +-------------------+   +-------------------+

  +-------------------+   +-------------------+
  |   Hall Sensor 4   |   |   Hall Sensor 5   |
  |  (RIGHT-CLICK) 🖱️ |   |  (Cursor Move)    |
  |                   |   |                   |
  |  VCC ── 3.3V      |   |  VCC ── 3.3V      |
  |  GND ── GND       |   |  GND ── GND       |
  |  DOUT── GPIO26    |   |  DOUT── GPIO27    |
  +-------------------+   +-------------------+
              |
  +-----------+------------------------------+
  |                   ESP32                  |
  |                                          |
  |  GPIO32 ── Sensor 1 (Cursor)             |
  |  GPIO33 ── Sensor 2 (Cursor)             |
  |  GPIO25 ── Sensor 3 (Cursor)             |
  |  GPIO26 ── Sensor 4 (Right-Click)        |
  |  GPIO27 ── Sensor 5 (Cursor)             |
  |  VIN    ── Power Supply                  |
  |  GND    ── Common Ground                 |
  +------------------------------------------+
              |
         USB Serial
              |
  +-----------+------------------------------+
  |          PC — Python Script              |
  |                                          |
  |  pyserial  ── reads serial data          |
  |  pyautogui ── moves cursor / clicks      |
  +------------------------------------------+
```

---

## 🚀 Installation & Setup

### Step 1 — Upload ESP32 Code

1. Open **Arduino IDE**
2. Connect the **ESP32** to your PC via USB
3. Go to `Tools → Board` and select **ESP32**
4. Go to `Tools → Port` and select the correct COM port
5. Open the sketch file: `magnetic_cursor.ino`
6. Click **Upload** ⬆️

> ⚠️ Ensure all five Hall effect sensors are correctly connected to their respective GPIO pins before uploading.

---

### Step 2 — Connect the Hall Effect Sensors

Make the following connections for each sensor:

```
Sensor VCC   →  3.3V (ESP32)
Sensor GND   →  GND
Sensor DOUT  →  GPIO32 / GPIO33 / GPIO25 / GPIO26 / GPIO27
```

> ⚠️ All sensors must share a **common ground** with the ESP32 for correct readings.

---

### Step 3 — Power the System

Power the ESP32 using one of the following:
- USB connection from your PC
- External 5V supply connected to the **VIN pin**

Verify that the ESP32 boots up correctly (onboard LED or serial monitor output).

---

### Step 4 — Run the Python Script

1. Close the **Arduino IDE Serial Monitor** if it is open — Python needs exclusive access to the serial port
2. Set the correct COM port in the Python script:

```python
SERIAL_PORT = "COM3"           # Windows
# SERIAL_PORT = "/dev/ttyUSB0"  # Linux / Mac
```

3. Run the script:

```bash
python magnetic_cursor.py
```

---

### Step 5 — Test the System

- Hold the **neodymium magnet** above the sensor array
- Move it over each of the four cursor sensors to control mouse movement
- Hover over **Sensor 4 (GPIO26)** to trigger a **right-click**
- Open the serial monitor (before running Python) to verify raw sensor values are being transmitted correctly

---

## 📝 Notes & Tips

- **Common ground is essential** — all sensors and the ESP32 must share a ground reference for correct readings
- The sensors output a **digital HIGH or LOW** based on magnet presence — no analog thresholding needed
- **Magnet orientation matters** — flip the magnet if a sensor is not triggering as expected
- Use a **stable power supply** — voltage fluctuations can cause false triggers
- **Keep the magnet away from sensors when not in use** — an idle magnet resting over the array may cause unintended inputs
- **GPIO26 is reserved for right-click** — place this sensor in an easily reachable position on the glove or fixture

---

## 🛠️ Troubleshooting

### ❌ Sensor Not Triggering
- Check that **VCC and GND connections are secure**
- Ensure the **magnet is close enough** to the sensor surface
- **Flip the magnet** — the sensor may only respond to one pole

### 📉 False or Erratic Triggers
- Provide a **stable 3.3V supply** to all sensors
- Shield the sensor array from **nearby metal objects or other magnets**
- Check all wiring for **loose connections**
- Add a small delay in the Arduino loop to debounce rapid triggers

### 🖱️ Cursor Not Moving or Right-Click Not Working
- Ensure the **Arduino IDE Serial Monitor is fully closed** before running the Python script
- Verify the correct **COM port** is set in the Python script
- Confirm that `pyserial` and `pyautogui` are both installed: `pip install pyserial pyautogui`
- Double-check that **GPIO26** is correctly wired to the right-click sensor

### 🔌 ESP32 Not Detected in Arduino IDE
- Install the **ESP32 board package**: `File → Preferences → Additional Boards Manager URLs`
  - Add: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
  - Then go to `Tools → Board → Boards Manager` and search **ESP32**
- Verify the correct **COM port** is selected under `Tools → Port`
- Try a **different USB cable** — some cables are charge-only and won't transmit data

---

## 📁 Project Structure

```
contactless-magnetic-cursor/
├── magnetic_cursor.ino       # ESP32 Arduino sketch
├── magnetic_cursor.py        # Python cursor control script
└── README.md                 # This file
```

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
