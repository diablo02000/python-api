import platform
import time
import tomllib
from functools import lru_cache
from pathlib import Path as path

from fastapi import FastAPI

app = FastAPI()


def get_project_file() -> str:
    """Get the path to the project file"""
    app_basedir = path(__file__).parent.parent
    return str(app_basedir.joinpath("pyproject.toml"))


@lru_cache
def get_hostname() -> str:
    """Get the hostname of the machine"""
    return platform.node()


@lru_cache
def get_version() -> str:
    """Get the version of the project"""
    with open(get_project_file(), mode="rb") as f:
        return tomllib.load(f)["project"]["version"]


@app.get("/status")
def status():
    """Get the status of the service"""
    return {"status": "running"}


@app.get("/whoami")
def whoami():
    """Get the hostname of the machine"""
    return {"hostname": get_hostname()}


@app.get("/version")
def version():
    """Get the version of the project"""
    return {"version": get_version()}


@app.get("/pause")
def pause(second: int = 0):
    """Pause the service
    :param second: The number of seconds to pause
    """
    time.sleep(second)
    return {"status": "succeed", "second": second}
