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

⚙️ How to Run
📟 Arduino
Upload the sketch (soil_sensors.ino) to your Arduino. It reads moisture + humidity and prints JSON over serial.

poetry install
poetry run python mqtt_publisher.py

📥 Telegraf
Configure telegraf.conf to consume MQTT topic and forward to InfluxDB.

📦 InfluxDB + Grafana
Run both in Docker (using mapped ports):

docker run -d -p 8086:8086 influxdb:2.7
docker run -d -p 3000:3000 grafana/grafana

🌐 Flask Web App
poetry run python app.py

📊 Grafana Dashboards
Sensor Trends (soil_moisture_1, 2, 3)

Real-time gauges with color-coded thresholds

Embedded in Flask UI

🚀 Future Enhancements
Automatic irrigation control (relays)

Alerts via SMS/email

Integration with weather APIs

Mobile app dashboard




