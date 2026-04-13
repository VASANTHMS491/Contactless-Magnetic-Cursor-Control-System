# 🧲 Contactless Magnetic Cursor Control System

> A touchless cursor control system using analog Hall effect sensors and ESP32 — powered by magnetic field sensing and Python-based mouse control.

---

## 📖 Description

This project implements a contactless cursor control system using multiple analog Hall effect sensors. A small permanent magnet is used as the input device, and its movement is detected through variations in magnetic field strength.

The ESP32 reads analog values from multiple sensors, determines directional movement based on relative changes, and transmits the data to a computer via serial communication. A Python script interprets this data and controls the cursor using `pyautogui`.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧲 Contactless Control | No physical touch required for cursor movement |
| 📡 Real-Time Detection | Instant response to magnet movement |
| 🎯 Direction Mapping | Detects left, right, up, and down movement |
| 🖱️ Cursor Control | Python script converts sensor data into mouse movement |
| ⚡ Low Cost | Built using simple analog sensors |
| 🔧 Easy Implementation | No complex hardware or protocols required |

---

## 🔧 Hardware Components

### 1. ESP32
Reads analog values from sensors and sends data via serial communication.

### 2. Analog Hall Effect Sensors (49E-type)
Detect magnetic field strength and output corresponding analog voltage.

### 3. Neodymium Magnet
Acts as the input device for cursor control.

### 4. Breadboard & Jumper Wires
Used for prototyping and connections.

---

## 💻 Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software)
- Python 3.x
- Required Python libraries:
```bash
pip install pyserial pyautogui
