sensors = {
    "DHT11": {
        # "_id": "65dd080111bbe96dbfe4b2d2",
        "type": "Sensor",
        "name": "Temperatura y Humedad",
        "brand": "Genérico",
        "model": "DHT11",
        "specifications": [
            {
                "name": "Rango de medición de temperatura",
                "minValue": 0.0,
                "maxValue": 50.0,
                "unit": "°C",
            },
            {
                "name": "Rango de medición de humedad",
                "minValue": 20.0,
                "maxValue": 90.0,
                "unit": "%",
            },
            {
                "name": "Voltage de operación",
                "value": 5.5,
                "unit": "V",
            },
            {
                "name": "Corriente de operación",
                "value": 2.5,
                "unit": "mA",
                "type": "VCD",
            },
            {
                "name": "Consumo eléctrico",
                "value": 0.00125,
                "unit": "W",
            },
        ],
        "location": "",
        "status": "Disponible",
        "initialDate": 0,
        "owner": "MAHITECH-Haziel",
        "startsAt": 0,
        "endsAt": 0,
        "readings": [
            {
                "name": "Detección de Temperatura",
                "value": 0.00,
                "measuramentUnit": "°C",
            },
            {
                "name": "Detección de Humedad",
                "value": 0.00,
                "measuramentUnit": "%",
            },
        ],
    },
    "LDR": {
        # "_id": {"$oid": "65dd0b0611bbe96dbfe4b2d4"},
        "type": "Sensor",
        "name": "Fotoresistencia",
        "brand": "Genérico",
        "model": "LDR",
        "specifications": [
            {
                "name": "Rango espectral",
                "minValue": 400.0,
                "maxValue": 700.0,
                "unit": "nm",
            },
            {"name": "Rango de respuesta", "minValue": 0, "maxValue": 1024},
            {
                "name": "Voltage de operación",
                "value": 5.0,
                "unit": "V",
            },
            {
                "name": "Corriente de operación",
                "value": 0.45,
                "unit": "mA",
                "type": "VCD",
            },
            {
                "name": "Consumo de operación",
                "value": 1.56,
                "unit": "W",
            },
        ],
        "location": "",
        "status": "Disponible",
        "initialDate": 0,
        "owner": "MAHITECH-Haziel",
        "startsAt": 0,
        "endsAt": 0,
        "readings": [
            {
                "name": "Detección de iluminación",
                "value": 0,
            }
        ],
    },
}
