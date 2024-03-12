from datetime import datetime as dt

rooms = [
    "Recámara 1",
    "Recámara 2",
    "Recámara 3",
    "Baño 1",
    "Baño 2",
    "Cocina",
    "Garaje",
    "Sala de estar",
]

roomsData = {
    "bedrooms": [
        {
            # "_id": "65dd080111bbe96dbfe4b2d2",
            "type": "Sensor",
            "name": "Sensor de temperatura y humedad",
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
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 12, 0, 0).timestamp(),
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 13, 0, 0).timestamp(),
            "endsAt": dt(2024, 3, 11, 13, 0, 5).timestamp(),
            "readings": [
                {
                    "name": "Detección de Temperatura",
                    "value": 30.5,
                    "measuramentUnit": "°C",
                },
                {
                    "name": "Detección de Humedad",
                    "value": 25.0,
                    "measuramentUnit": "%",
                },
            ],
        },
        {
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
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 13, 30, 0).timestamp,
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 13, 30, 0).timestamp,
            "endsAt": dt(2024, 3, 11, 13, 30, 5).timestamp,
            "readings": [
                {
                    "name": "Detección de iluminación",
                    "value": 600.0,
                }
            ],
        },
        {
            # "_id": {"$oid": "65dd0e5511bbe96dbfe4b2d5"},
            "type": "Actuador",
            "name": "Relevador",
            "brand": "Songle",
            "model": "SRD-05VDC-SLC",
            "specifications": [
                {
                    "name": "Interrupciones mecánicas",
                    "value": 300.0,
                    "unit": "operaciones/minuto",
                },
                {
                    "name": "Interrupciones eléctricas",
                    "value": 30.0,
                    "unit": "operaciones/minuto",
                },
                {
                    "name": "Voltage de operación",
                    "value": 5.0,
                    "unit": "V",
                },
                {"name": "Tipo de corriente", "value": "DC"},
                {
                    "name": "Corriente de operación",
                    "value": 10.0,
                    "unit": "mA",
                    "type": "VCD",
                },
                {
                    "name": "Consumo eléctrico",
                    "value": 0.25,
                    "unit": "W",
                },
            ],
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 13, 20, 0).timestamp(),
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 13, 20, 0).timestamp(),
            "endsAt": dt(2024, 3, 11, 13, 20, 5).timestamp(),
            "actions": [{"name": "Acticación mecánica", "value": "Activado"}],
        },
        {
            # "_id": {"$oid": "65d4f24c14a33a3563f3d1ee"},
            "type": "Actuador",
            "name": "Ventilador",
            "brand": "SY",
            "model": "DC BRUSHLESS FAN",
            "specifications": [
                {"name": "Tamaño", "value": 30.0, "unit": "mm"},
                {"name": "Peso", "value": 9.0, "unit": "g"},
                {"name": "Sonido", "value": 25.0, "unit": "dB"},
                {
                    "name": "Velocidad de operación",
                    "value": 8000.0,
                    "unit": "rpm",
                },
                {
                    "name": "Desplazamiento de aire",
                    "value": 3.3,
                    "unit": "cfm",
                },
                {
                    "name": "Voltage de operación",
                    "value": 5.0,
                    "unit": "V",
                },
                {
                    "name": "Corriente de operación",
                    "value": 0.13,
                    "unit": "A",
                    "type": "VCD",
                },
                {
                    "name": "Consumo eléctrico",
                    "value": 1.56,
                    "unit": "W",
                },
            ],
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 13, 40, 0).timestamp(),
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 13, 40, 0).timestamp(),
            "endsAt": dt(2024, 3, 11, 13, 40, 5).timestamp(),
            "actions": [{"name": "Acticación mecánica", "value": "30", "unit": "%"}],
        },
        {
            # "_id": {"$oid": "65dd0ff411bbe96dbfe4b2d6"},
            "type": "Actuador",
            "name": "Micro Servomotor 1",
            "brand": "TowerPro",
            "model": "SG90",
            "specifications": [
                {
                    "name": "Velocidad de operación",
                    "value": 0.12,
                    "unit": "segundos/60°",
                },
                {"name": "Torque", "value": 2.5, "unit": "kg-cm"},
                {
                    "name": "Voltage de operación",
                    "value": 5.0,
                    "unit": "V",
                },
                {
                    "name": "Corriente de operación",
                    "value": 10.0,
                    "unit": "mA",
                    "type": "VCD",
                },
                {
                    "name": "Consumo eléctrico",
                    "value": 0.5,
                    "unit": "W",
                },
            ],
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 13, 50,0).timestamp(),
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 13, 50,0).timestamp(),
            "endsAt": dt(2024, 3, 11, 13, 50,5).timestamp(),
            "actions": [
                {
                    "name": "Acticación mecánica",
                    "value": "90",
                    "unit": "°",
                    "status": "Interrumpido",
                }
            ],
        },
        {
            # "_id": {"$oid": "65dd0ff411bbe96dbfe4b2d6"},
            "type": "Actuador",
            "name": "Micro Servomotor 1",
            "brand": "TowerPro",
            "model": "SG90",
            "specifications": [
                {
                    "name": "Velocidad de operación",
                    "value": 0.12,
                    "unit": "segundos/60°",
                },
                {"name": "Torque", "value": 2.5, "unit": "kg-cm"},
                {
                    "name": "Voltage de operación",
                    "value": 5.0,
                    "unit": "V",
                },
                {
                    "name": "Corriente de operación",
                    "value": 10.0,
                    "unit": "mA",
                    "type": "VCD",
                },
                {
                    "name": "Consumo eléctrico",
                    "value": 0.5,
                    "unit": "W",
                },
            ],
            "location": "Recámara 3",
            "status": "Disponible",
            "initialDate": dt(2024, 3, 11, 14, 50,0).timestamp(),
            "owner": "MAHITECH-Haziel",
            "startsAt": dt(2024, 3, 11, 14, 50,0).timestamp(),
            "endsAt": dt(2024, 3, 11, 14, 50,5).timestamp(),
            "actions": [
                {
                    "name": "Acticación mecánica",
                    "value": "90",
                    "unit": "°",
                    "status": "Interrumpido",
                }
            ],
        },
    ],
    "livingrooms": [],
    "kitchens": [],
    "bathrooms": [],
    "garages": [],
}
