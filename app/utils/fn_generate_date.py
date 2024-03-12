# Generar una función que nos permita generar fechas aleatorias en formato requerido en Mongo, considerar fecha y hora límites válidos.
from datetime import datetime as dt;
from .fn_generate_rand_int import fn_generate_rand_int as randInt;

def fn_generate_date(
    yearMinLimit: int,
    yearMaxLimit: int, 
    monthMinLimit: int, 
    monthMaxLimit: int, 
    dayMinLimit: int, 
    dayMaxLimit: int, 
    hoursMinLimit: int, 
    hoursMaxLimit: int, 
    minutesMinLimit: int, 
    minutesMaxLimit: int,
    secondsMinLimit: int,
    secondsMaxLimit: int
) -> dict :
    randomTimestamp = dt(
        randInt(yearMinLimit, yearMaxLimit),
        randInt(monthMinLimit, monthMaxLimit),
        randInt(dayMinLimit, dayMaxLimit),
        randInt(hoursMinLimit, hoursMaxLimit),
        randInt(minutesMinLimit, minutesMaxLimit),
        randInt(secondsMinLimit, secondsMaxLimit)
    ).timestamp()


    return {
        "$date": {
            "$numberlong": str(randomTimestamp) 
        }
    }