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
    "bedrooms": {
        "sensors": [
            #Recámara 3: Sensor - DHT11  (MAHITECH)
            {
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
                    {"name": "Voltage de operación", "value": 5.5, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 2.5,
                        "unit": "mA",
                        "type": "VCD",
                    },
                    {"name": "Consumo eléctrico", "value": 0.00125, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
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
            #Recámara 3: Sensor - LDR  (MAHITECH)
            {
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
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 0.45,
                        "unit": "mA",
                        "type": "VCD",
                    },
                    {"name": "Consumo de operación", "value": 1.56, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "readings": [{"name": "Detección de iluminación", "value": 600.0}],
            },
        ],
        "actuators": [
            #Recámara 3: Actuador - Led Interior (MAHITECH)
            {
                "type": "Actuador",
                "name": "Led Interior",
                "brand": "Genérico",
                "model": "Diodo LED",
                "specifications": [
                    
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 5.0,
                        "unit": "mA",
                        "type": "VCD",
                    }
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [{"name": "Activación eléctrica", "value": "Activado"}],
            },
            #Recámara 3: Actuador - Led Exterior (MAHITECH)
            {
                "type": "Actuador",
                "name": "Led Exterior",
                "brand": "Genérico",
                "model": "Diodo LED",
                "specifications": [
                    
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 5.0,
                        "unit": "mA",
                        "type": "VCD",
                    }
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [{"name": "Activación eléctrica", "value": "Activado"}],
            },
            #Recámara 3: Actuador - Ventilador (MAHITECH)
            {
                "type": "Actuador",
                "name": "Ventilador",
                "brand": "SY",
                "model": "DC BRUSHLESS FAN",
                "specifications": [
                    {"name": "Tamaño", "value": 30.0, "unit": "mm"},
                    {"name": "Peso", "value": 9.0, "unit": "g"},
                    {"name": "Sonido", "value": 25.0, "unit": "dB"},
                    {"name": "Velocidad de operación", "value": 8000.0, "unit": "rpm"},
                    {"name": "Desplazamiento de aire", "value": 3.3, "unit": "cfm"},
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 0.13,
                        "unit": "A",
                        "type": "VCD",
                    },
                    {"name": "Consumo eléctrico", "value": 1.56, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [
                    {"name": "Activación mecánica", "value": "30", "unit": "%"}
                ],
            },
            #Recámara 3: Actuador - Servomotor 1 - Puerta (MAHITECH)
            {
                "type": "Actuador",
                "name": "Servomotor Puerta",
                "brand": "TowerPro",
                "model": "SG90",
                "specifications": [
                    {
                        "name": "Velocidad de operación",
                        "value": 0.12,
                        "unit": "segundos/60°",
                    },
                    {"name": "Torque", "value": 2.5, "unit": "kg-cm"},
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 10.0,
                        "unit": "mA",
                        "type": "VCD",
                    },
                    {"name": "Consumo eléctrico", "value": 0.5, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [
                    {
                        "name": "Activación mecánica",
                        "value": "90",
                        "unit": "°",
                        "status": "Interrumpido",
                    },
                ],
            },
            #Recámara 3: Actuador - Servomotor 2 - Ventana Doble Izquierda (MAHITECH)
            {
                "type": "Actuador",
                "name": "Servomotor Ventana Doble Izquierda",
                "brand": "TowerPro",
                "model": "SG90",
                "specifications": [
                    {
                        "name": "Velocidad de operación",
                        "value": 0.12,
                        "unit": "segundos/60°",
                    },
                    {"name": "Torque", "value": 2.5, "unit": "kg-cm"},
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 10.0,
                        "unit": "mA",
                        "type": "VCD",
                    },
                    {"name": "Consumo eléctrico", "value": 0.5, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [
                    {
                        "name": "Activación mecánica",
                        "value": "90",
                        "unit": "°",
                        "status": "Interrumpido",
                    },
                ],
            },
            #Recámara 3: Actuador - Servomotor 3 - Ventana Doble Derecha (MAHITECH)
            {
                "type": "Actuador",
                "name": "Micro Servomotor Ventana Doble Derecha",
                "brand": "TowerPro",
                "model": "SG90",
                "specifications": [
                    {
                        "name": "Velocidad de operación",
                        "value": 0.12,
                        "unit": "segundos/60°",
                    },
                    {"name": "Torque", "value": 2.5, "unit": "kg-cm"},
                    {"name": "Voltage de operación", "value": 5.0, "unit": "V"},
                    {
                        "name": "Corriente de operación",
                        "value": 10.0,
                        "unit": "mA",
                        "type": "VCD",
                    },
                    {"name": "Consumo eléctrico", "value": 0.5, "unit": "W"},
                ],
                "location": "Recámara 3",
                "status": "Disponible",
                "initialDate": {"$date": {"$numberLong": "1708580700000"}},
                "owner": "MAHITECH",
                "startsAt": {"$date": {"$numberLong": "1708580700000"}},
                "endsAt": {"$date": {"$numberLong": "1708580705000"}},
                "actions": [
                    {
                        "name": "Activación mecánica",
                        "value": "90",
                        "unit": "°",
                        "status": "Interrumpido",
                    },
                ],
            },
        ],
    },
    "livingrooms": {"sensors": [], "actuators": []},
    "kitchens": {"sensors": [], "actuators": []},
    "bathrooms": {"sensors": [], "actuators": []},
    "garages": {"sensors": [], "actuators": []},
}
