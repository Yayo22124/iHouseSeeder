from fastapi import APIRouter, Query
from ..utils.fn_generate_rand_int import fn_generate_rand_int
from ..utils.fn_generate_rand_decimal import fn_generate_rand_decimal
from ..utils.fn_generate_sensor_data import fn_generate_sensor_data
from ..utils.fn_generate_actuator_data import fn_generate_actuator_data
from ..models.rooms import rooms

# from ..controllers.homeworkControllers

homework_router = APIRouter(prefix="/functions", tags=["functions"])


@homework_router.get("/")
async def get_options() -> dict:
    return {
        "options": [
            {
                "name": "Get RandInt",
                "path": "/randint/?minLimit=0&maxLimit=10",
                "desc": "Get a random integer number between min and max limits.",
            },
            {
                "name": "Get RandDecimal",
                "path": "/randdecimal/?minLimit=0&maxLimit=10&numberDecimals=2",
                "desc": "Get a random decimal number with min and max limit, but also specific number of decimals.",
            },
            {
                "name": "Get RandLocation",
                "path": "/randlocation/",
                "desc": "Get a random room or location.",
            },
        ]
    }


@homework_router.get("/randint/")
async def get_randint(
    # Query Params
    minLimit: int = Query(0, description="Min limit of range."),
    maxLimit: int = Query(10, description="Max limit of range."),
) -> dict:
    randint: int = fn_generate_rand_int(minLimit, maxLimit)

    return {"result": randint}


@homework_router.get("/randdecimal/")
async def get_randint(
    # Query Params
    minLimit: int = Query(0, description="Min limit of range."),
    maxLimit: int = Query(10, description="Max limit of range."),
    numberDecimals: int = Query(2, description="Number of decimals."),
) -> dict:
    randDecimal: int = fn_generate_rand_decimal(minLimit, maxLimit, numberDecimals)

    return {"result": randDecimal}

@homework_router.get("/randlocation/")
async def get_randlocation() -> dict:
    randLocation: int = fn_generate_rand_int(0, len(rooms) - 1);

    return {"result": rooms[randLocation]}

@homework_router.get("/randsensor/")
async def get_randint(
    # Query Params
    sensorName: str = Query("DHT11", description="Sensor type to generate data."),
    location: str = Query("Recámara 1", description="Location of sensor."),
) -> dict:

    return fn_generate_sensor_data(location, sensorName);

@homework_router.get("/randactuator/")
async def get_randint(
    # Query Params
    actuatorName: str = Query("SRD", description="Actuator type to generate data."),
    location: str = Query("Recámara 1", description="Location of actuator."),
) -> dict:

    return fn_generate_actuator_data(location, actuatorName);
