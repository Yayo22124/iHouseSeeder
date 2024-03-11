# Generar una función que dado un espacio y un actuador genere acciones aleatorias (en un ambiente controlado siguiendo los valores válidos del actuador)
from datetime import datetime as dt, timedelta
from .fn_generate_rand_decimal import fn_generate_rand_decimal as randDecimal
from .fn_generate_rand_int import fn_generate_rand_int as randInt
from ..models.actuators import actuators


def fn_generate_actuator_data(location: str, actuator_name: str) -> dict:
    actuator = actuators.get(actuator_name)

    if not actuator:
        return {"msg": f"{actuator_name} not fount in actuators list."}

    currentDate = dt.now()
    endDate = dt.now() + timedelta(seconds=5)


    if actuator_name == "SRD":
        value = randInt(0, 1);
        if value == 1:    
            actions = [
                {
                    "name": "Acticación mecánica",
                    "value": "Activado"  
                }
            ]
        else :
            actions = [
                {
                    "name": "Acticación mecánica",
                    "value": "Desactivado"  
                }
            ]
        
    if actuator_name == "LDR":
        actions = [{"name": "Detección de Iluminación", "value": randInt(0, 1024)}]

    actuatorData = {
        "type": actuator["type"],
        "name": actuator["name"],
        "brand": actuator["brand"],
        "model": actuator["model"],
        "specifications": actuator["specifications"],
        "location": location,
        "status": actuator["status"],
        "initialDate": currentDate,
        "owner": actuator["owner"],
        "startsAt": currentDate,
        "endsAt": endDate,
        "actions": actions,
    }

    return actuatorData
