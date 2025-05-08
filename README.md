# IOT_EcoGro# 🌱 IOT_EcoGrow - Smart Soil Monitoring System

IOT_EcoGrow is a smart, end-to-end IoT system for real-time soil moisture and humidity monitoring. It collects sensor data via Arduino, transmits it securely via MQTT to HiveMQ Cloud, stores it in InfluxDB using Telegraf, and visualizes it with Grafana. A Flask web app also provides a friendly UI with live graphs and dynamic plant status GIFs.

---

## 📸 Features

- Real-time soil moisture and humidity monitoring
- Secure MQTT communication with HiveMQ Cloud
- Time-series data storage with InfluxDB
- Beautiful dashboards using Grafana
- Flask web app displaying animated plant health status
- Easily scalable and modular

---

## 🔧 System Architecture

![ChatGPT Image May 7 2025 IOT Project Ideas](https://github.com/user-attachments/assets/8412a5e5-e85f-4d7a-8675-64b9038a15b1)

# ⚙️ How to Run
📟 Arduino Setup
Upload the soil_sensors.ino sketch to your Arduino board.

It reads analog soil moisture and DHT22 humidity/temperature data.

Outputs JSON over serial to the connected computer.

# Python MQTT Publisher
poetry install
poetry run python mqtt_publisher.py
Reads serial data from Arduino

Publishes it securely to HiveMQ Cloud over MQTT

# 📥 Telegraf (MQTT Consumer)
Configure telegraf.conf with:

Input: [[inputs.mqtt_consumer]] for topic soil/sensor_data

Output: [[outputs.influxdb_v2]] pointing to your InfluxDB container

📦 InfluxDB + Grafana (Data Storage & Visualization)
Start the containers using Docker:

# InfluxDB
docker run -d -p 8086:8086 influxdb:2.7

# Grafana
docker run -d -p 3000:3000 \
  -e GF_SECURITY_ALLOW_EMBEDDING=true \
  -e GF_SECURITY_ADMIN_PASSWORD=admin@123 \
  grafana/grafana

# Flask Web App
poetry run python app.py
Fetches the latest moisture value from InfluxDB using Flux

Displays plant status (healthy/dry/overwatered) using dynamic GIFs

# Future Enhancements
- Automatic irrigation using relays and moisture logic
- Mobile dashboard view and remote access
- Weather API integration for smarter decisions
- Real-time alerts via email/SMS on dry soil






