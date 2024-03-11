# Generar una función que dado un espacio y un sensor genere lecturas aleatorias (en un ambiente controlado siguiendo los valores válidos de un sensor).
from datetime import datetime as dt, timedelta;
from .fn_generate_rand_decimal import fn_generate_rand_decimal as randDecimal;
from .fn_generate_rand_int import fn_generate_rand_int as randInt;
from ..models.sensors import sensors;

def fn_generate_sensor_data(location: str, sensor_name: str) -> dict:
    sensor = sensors.get(sensor_name);
    
    if not sensor :
        return {
            "msg": f"{sensor_name} not fount in sensors list."
        }

    currentDate = dt.now();
    endDate = dt.now() + timedelta(seconds=5);
    if sensor_name == "DHT11":
        readings = [
            {
                "name": "Detección de Temperatura",
                "value": randDecimal(0, 50, 2),
                "measuramentUnit": "˚C"
            },
            {
                "name": "Detección de Humedad",
                "value": randInt(0, 90),
                "measuramentUnit": "%"
            },
        ]
    if sensor_name == "LDR":
        readings = [
            {
                "name": "Detección de Iluminación",
                "value": randInt(0, 1024)
            }
        ]

    sensorData = {
        "type": sensor["type"],
        "name": sensor["name"],
        "brand": sensor["brand"],
        "model": sensor["model"],
        "specifications": sensor["specifications"],
        "location": location,
        "status": sensor["status"],
        "initialDate": currentDate,
        "owner": sensor["owner"],
        "startsAt": currentDate,
        "endsAt": endDate,
        "readings": readings,
    }

    return sensorData;
