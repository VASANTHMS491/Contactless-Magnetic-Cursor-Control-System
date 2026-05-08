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

A contactless cursor control system that uses multiple **analog Hall effect sensors (49E-type)** to detect the movement of a small permanent magnet. As the magnet moves, variations in magnetic field strength are detected across sensors, allowing the system to determine directional movement.

The ESP32 reads analog values from all sensors, determines the direction of magnet movement based on relative field changes, and transmits the data to a computer via **serial communication**. A Python script interprets this data and controls the cursor using `pyautogui`.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧲 **Contactless Control** | No physical touch required for cursor movement |
| 📡 **Real-Time Detection** | Instant response to magnet position changes |
| 🎯 **Direction Mapping** | Detects left, right, up, and down movement |
| 🖱️ **Cursor Control** | Python script converts sensor data into mouse movement |
| 💰 **Low Cost & Scalable** | Built with affordable, off-the-shelf components |
| ⚡ **Continuous Detection** | Detects movement instantly — no manual input needed |
| 🔧 **Easy Implementation** | No complex hardware protocols required |

---

## 🔧 Hardware Components

### 1. ESP32
Reads analog values from Hall effect sensors via ADC pins, determines directional movement, and transmits data to the PC via serial communication.

### 2. Analog Hall Effect Sensors — 49E-type
Detect magnetic field strength and output a corresponding analog voltage. Multiple sensors are arranged spatially to determine the direction of magnet movement.

### 3. Neodymium Magnet
Acts as the primary input device. Moving the magnet above or around the sensor array produces directional control signals.

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
| `pyautogui` | Moves the cursor based on detected direction |

---

## 🔌 Pin Connections

| Component | Pin | Connected To |
|---|---|---|
| Hall Sensor 1 (Left) | VCC | 3.3V (ESP32) |
| Hall Sensor 1 (Left) | GND | GND |
| Hall Sensor 1 (Left) | Analog Output | GPIO34 (ADC Pin) |
| Hall Sensor 2 (Right) | VCC | 3.3V (ESP32) |
| Hall Sensor 2 (Right) | GND | GND |
| Hall Sensor 2 (Right) | Analog Output | GPIO35 (ADC Pin) |
| Hall Sensor 3 (Up) | VCC | 3.3V (ESP32) |
| Hall Sensor 3 (Up) | GND | GND |
| Hall Sensor 3 (Up) | Analog Output | GPIO32 (ADC Pin) |
| Hall Sensor 4 (Down) | VCC | 3.3V (ESP32) |
| Hall Sensor 4 (Down) | GND | GND |
| Hall Sensor 4 (Down) | Analog Output | GPIO33 (ADC Pin) |
| ESP32 | VIN | 5V Power Supply |
| ESP32 | GND | Common Ground |

### Wiring Diagram

```
  +---------------------+     +---------------------+
  |  Hall Sensor 1      |     |  Hall Sensor 2      |
  |     (LEFT)          |     |     (RIGHT)         |
  |                     |     |                     |
  |  VCC  ── 3.3V ──────┐     |  VCC  ── 3.3V ──────┤
  |  GND  ── GND  ───── ┤     |  GND  ── GND  ───── ┤
  |  AOUT ── GPIO34 ────┤     |  AOUT ── GPIO35 ────┤
  +---------------------+     +---------------------+

  +---------------------+     +---------------------+
  |  Hall Sensor 3      |     |  Hall Sensor 4      |
  |      (UP)           |     |     (DOWN)          |
  |                     |     |                     |
  |  VCC  ── 3.3V ──────┤     |  VCC  ── 3.3V ──────┤
  |  GND  ── GND  ───── ┤     |  GND  ── GND  ───── ┤
  |  AOUT ── GPIO32 ────┤     |  AOUT ── GPIO33 ────┤
  +---------------------+     +---------------------+
              |
  +-----------+----------------------------+
  |                  ESP32                 |
  |                                        |
  |  GPIO34 ── Sensor 1 (Left)             |
  |  GPIO35 ── Sensor 2 (Right)            |
  |  GPIO32 ── Sensor 3 (Up)               |
  |  GPIO33 ── Sensor 4 (Down)             |
  |  VIN    ── Power Supply                |
  |  GND    ── Common Ground               |
  +----------------------------------------+
              |
         USB Serial
              |
  +-----------+----------------------------+
  |         PC — Python Script             |
  |                                        |
  |  pyserial  ── reads serial data        |
  |  pyautogui ── moves cursor             |
  +----------------------------------------+
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

> ⚠️ Ensure all Hall effect sensors are correctly connected to their respective ADC pins before uploading.

---

### Step 2 — Connect the Hall Effect Sensors

Make the following connections for each sensor:

```
Sensor VCC   →  3.3V (ESP32)
Sensor GND   →  GND
Sensor AOUT  →  GPIO34 / GPIO35 / GPIO32 / GPIO33
```

Arrange the four sensors in a **2×2 cross pattern** on the breadboard:

```
        [Sensor 3 — Up]
              ↑
[Sensor 1]  ←  →  [Sensor 2]
   Left               Right
              ↓
        [Sensor 4 — Down]
```

> ⚠️ All sensors must share a **common ground** with the ESP32 for correct ADC readings.

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
SERIAL_PORT = "COM3"          # Windows
# SERIAL_PORT = "/dev/ttyUSB0"  # Linux / Mac
```

3. Run the script:

```bash
python magnetic_cursor.py
```

---

### Step 5 — Test the System

- Hold the **neodymium magnet** above the sensor array
- Move it **left, right, up, or down** over the corresponding sensor
- The Python script will detect the dominant sensor reading and move the cursor accordingly
- Open the serial monitor (before running Python) to verify raw sensor values are being transmitted correctly

---

## 📝 Notes & Tips

- **Common ground is essential** — all sensors and the ESP32 must share a ground reference for correct ADC readings
- The sensors output an **analog voltage proportional to magnetic field strength** — closer magnet = stronger signal = higher or lower voltage depending on polarity
- Always use **ADC-capable pins** — GPIO34, GPIO35, GPIO32, GPIO33 are all input-only ADC pins on the ESP32, ideal for sensing
- **Magnet orientation matters** — flip the magnet if sensor readings are inverted compared to expected direction
- Use a **stable power supply** — voltage fluctuations will cause noisy ADC readings and erratic cursor movement
- **Keep the magnet away from the sensors when not in use** — a resting magnet above the array will produce a constant offset in all readings

---

## 🛠️ Troubleshooting

### ❌ Sensor Not Giving Proper Readings
- Verify **AOUT is connected to an ADC-capable pin** (GPIO34, GPIO35, GPIO32, GPIO33)
- Check that **VCC and GND connections are secure**
- Ensure the **magnet is close enough** to the sensor — neodymium magnets typically need to be within 2–5 cm for reliable readings

### 📉 Unstable or Noisy Sensor Values
- Provide a **stable 3.3V supply** to all sensors
- Shield the sensor array from **nearby metal objects or other magnets**
- Check all wiring for **loose connections**
- Add a small delay in the Arduino loop to allow ADC readings to settle

### 🖱️ Cursor Not Moving or Moving Erratically
- Ensure the **Arduino IDE Serial Monitor is fully closed** before running the Python script
- Verify the correct **COM port** is set in the Python script
- Check that `pyserial` and `pyautogui` are both installed: `pip install pyserial pyautogui`
- Increase the **sensitivity threshold** in the Python script if the cursor moves on its own without magnet movement

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
