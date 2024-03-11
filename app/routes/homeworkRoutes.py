from fastapi import APIRouter, Query
from ..utils.fn_generate_rand_int import fn_generate_rand_int
from ..utils.fn_generate_rand_decimal import fn_generate_rand_decimal

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
