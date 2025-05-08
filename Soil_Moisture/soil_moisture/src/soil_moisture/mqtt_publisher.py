import serial
import json
import time
import paho.mqtt.client as mqtt

# ====== Serial Settings ======
SERIAL_PORT = '/dev/cu.usbmodem11301' 
BAUD_RATE = 9600

# ====== MQTT Settings (HiveMQ Cloud) ======
MQTT_BROKER = 'd949160b0d3b4777b49f198fafdee11a.s1.eu.hivemq.cloud'
MQTT_PORT = 8883
MQTT_TOPIC = 'soil/sensor_data'
MQTT_USERNAME = 'User1'  
MQTT_PASSWORD = 'User@123'

# ====== Setup Serial Connection ======
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)

# ====== Define MQTT Callbacks ======
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HiveMQ Cloud successfully!")
    else:
        print(f"Failed to connect, return code {rc}")

# ====== Setup MQTT Client ======
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)  
client.tls_set()  # <-- Enable TLS/SSL encryption
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

print("Connecting to HiveMQ Cloud...")

# ====== Main Loop ======
try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                data = json.loads(line)
                data['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')

                payload = json.dumps(data)

                client.publish(MQTT_TOPIC, payload, qos=1, retain=True)
                print(f"Published: {payload}")

            except json.JSONDecodeError:
                print("Invalid JSON received:", line)

except KeyboardInterrupt:
    print("Stopped publishing.")
    ser.close()
    client.disconnect()
