import time

from fastapi import APIRouter

import app.utils as utils

router = APIRouter()


@router.get("/whoami")
def whoami():
    """Get the hostname of the machine"""
    return {"hostname": utils.get_hostname()}


@router.get("/pause")
def pause(second: int = 0):
    """Pause the service
    :param second: The number of seconds to pause
    """
    time.sleep(second)
    return {"status": "succeed", "second": second}
