from msgspec import Struct, field


class Settings(Struct):
    app_name: str = "Python API"
    allowed_hosts: list[str] = field(default_factory=list)
    debug: bool = False
