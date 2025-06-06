import platform
from functools import lru_cache

from app.models.configurations import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


@lru_cache
def get_hostname() -> str:
    """Get the hostname of the machine"""
    return platform.node()
