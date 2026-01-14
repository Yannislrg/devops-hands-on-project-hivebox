from fastapi import FastAPI
from datetime import datetime, timedelta
import requests

app = FastAPI()

BASE_URL = "https://api.opensensemap.org"
BOX_ID = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c",
]


@app.get("/version")
def print_version():
    """return the current version of the app

    Returns:
        _type_: return description
    """
    version = "0.0.2"
    return {"Application Version": version}


def too_old_data(sensor):
    """Check if the sensor data is older than 1 hour

    Args:
        sensor (_type_): sensor data
    Returns:
        bool: True if data is older than 1 hour, False otherwise
    """

    last_measurement_time = datetime.strptime(
        sensor["lastMeasurement"]["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    print("last measurement time:", last_measurement_time)
    if last_measurement_time:
        if datetime.now() - last_measurement_time > timedelta(hours=2):
            return True
    return False


@app.get("/temperature")
def get_avg_temperature():
    """return avg temperature value

    Returns:
        _type_: return avg temperature
    """
    temperature = 0.0
    for box_id in BOX_ID:
        response = requests.get(f"{BASE_URL}/boxes/{box_id}", timeout=30)
        data = response.json()
        for sensor in data.get("sensors", []):
            if sensor.get("title") != "Temperatur":
                continue
            if too_old_data(sensor):
                continue
            print("sensor data:", sensor)
            temperature += float(sensor["lastMeasurement"]["value"])

    temperature /= len(BOX_ID)
    rounded_temp = round(temperature, 4)
    if rounded_temp:
        return {"average_temperature": rounded_temp}
    return {"error": "No temperature data available"}
