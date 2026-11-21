# Real-Time-Anomaly-Detection-Alerting-System-IoT-Time-Series-
# Real-Time Anomaly Detection & Alerting System
### An IoT-Based Multisensor Predictive Maintenance System

## 1. Project Overview

This project aims to develop an intelligent Industrial IoT system for real-time machine condition monitoring and anomaly detection.

The system uses multiple sensors connected to an ESP32 microcontroller to continuously collect operational data from an electric motor, including vibration, acoustic signals, temperature, and electrical current.

The collected data is transmitted to a Python-based backend, where it is processed, stored, and analyzed using Machine Learning techniques to detect abnormal operating patterns.

When an anomaly is detected, the system generates alerts and displays the machine's condition through a web-based dashboard, enabling maintenance personnel to monitor machine health and take timely action.

## 2. System Architecture

The proposed architecture consists of five interconnected layers:

**1. Sensing Layer**
- Vibration Sensor
- Acoustic Sensor
- Temperature Sensor
- Current Sensor

Collects multiple physical measurements to monitor the operating condition of the electric motor.

**2. Data Acquisition Layer**
- ESP32 Microcontroller

Reads sensor measurements, performs basic processing, adds timestamps, and prepares the data for transmission.

**3. Communication and Backend Layer**
- Wi-Fi
- HTTP / MQTT
- Python (Flask)

Receives sensor data, validates incoming measurements, and manages communication between the hardware and software components.

**4. Data Storage and Machine Learning Layer**
- SQLite Database
- Machine Learning Model

Stores sensor readings and historical records. The ML model analyzes multivariate time-series data to identify abnormal operating patterns and generate anomaly scores.

**5. Application and Alert Layer**
- Flask Web Dashboard
- Telegram / Email Notifications
- LED / Buzzer (Local Alerts)

Visualizes real-time machine conditions, displays anomaly detection results, and notifies maintenance personnel when abnormal behavior is detected.

### Architecture Flow

Sensors → ESP32 → Wi-Fi (HTTP / MQTT) → Flask Backend → Database and ML Model → Alert Engine → Web Dashboard and Notifications