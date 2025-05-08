# File: app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

# Configuration
GRAFANA_EMBED_URL = "http://localhost:3000/d/eekwpz4pn36rka/soilmoisture"
GRAFANA_PANEL_ID = "1"
PLANT_IMAGE_RULES = {
    "healthy": "static/healthy.gif",
    "dry": "static/dry.gif",
    "overwatered": "static/overwatered.gif"
}
INFLUX_QUERY_URL = "http://localhost:8086/api/v2/query"  
INFLUX_TOKEN = "43bH0PJhIwT4lLDarlXLgsh3v1tTS0pvstqGat6RvM0KpmrD9aMjKhGG-7XSFxXpic9Kzubvk98eakErHAMYgw=="
ORG = "rowan"
BUCKET = "soil_data"


def get_latest_soil_value():
    flux_query = f'''
    from(bucket: "{BUCKET}")
      |> range(start: -3h)
      |> filter(fn: (r) => r._measurement == "soil_moisture")
      |> filter(fn: (r) => r._field == "soil_moisture_1")
      |> last()
    '''

    headers = {
        "Authorization": f"Token {INFLUX_TOKEN}",
        "Content-Type": "application/vnd.flux"
    }

    try:
        response = requests.post(
            INFLUX_QUERY_URL,
            params={"org": ORG},
            headers=headers,
            data=flux_query
        )

        print("Status Code:", response.status_code)
        print("Raw Response:\n", response.text)

        if response.status_code != 200:
            print("❌ InfluxDB Query Error:", response.text)
            return None

        # Parse CSV-like response to find _value
        for line in response.text.strip().split("\n"):
            if line.startswith("#"):
                continue  # skip metadata lines
            parts = line.split(",")
            try:
                value_str = parts[-1].strip()
                value = float(value_str)
                print("✅ Parsed Value:", value)
                return value
            except Exception as e:
                print("⚠️  Parsing error:", e)

    except Exception as e:
        print("❌ Exception while querying InfluxDB:", e)

    return None

    flux_query = f'''
    from(bucket: "{BUCKET}")
      |> range(start: -3h)
      |> filter(fn: (r) => r._measurement == "soil_moisture")
      |> filter(fn: (r) => r._field == "soil_moisture_1")
      |> last()
    '''

    headers = {
        "Authorization": f"Token {INFLUX_TOKEN}",
        "Content-Type": "application/vnd.flux"
    }

    response = requests.post(
        INFLUX_QUERY_URL,
        params={"org": ORG},
        headers=headers,
        data=flux_query
    )

    if response.status_code == 200:
        for line in response.text.splitlines():
            if line.startswith("#"):
                continue
            columns = line.split(",")
            if len(columns) > 0 and "_value" in line:
                try:
                    # Try parsing the value from the last column
                    value = float(columns[-1].split()[-1])
                    return value
                except Exception as e:
                    print("Parsing error:", e)
    else:
        print("InfluxDB Query Error:", response.text)
    return None


def get_plant_status(value):
    if value is None:
        return "unknown", PLANT_IMAGE_RULES["overwatered"]
    if value < 200:
        return "overwatered", PLANT_IMAGE_RULES["overwatered"]
    elif value < 450:
        return "dry", PLANT_IMAGE_RULES["dry"]
    else:
        return "healthy", PLANT_IMAGE_RULES["healthy"]


@app.route("/")
def index():
    value = get_latest_soil_value()
    status, plant_gif = get_plant_status(value)
    grafana_url = f"{GRAFANA_EMBED_URL}?orgId=1&panelId={GRAFANA_PANEL_ID}&refresh=10s&theme=light"
    return render_template("index.html", value=value, status=status, gif_url=plant_gif, grafana_url=grafana_url)


if __name__ == "__main__":
    app.run(debug=True)
