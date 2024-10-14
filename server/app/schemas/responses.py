from pydantic import BaseModel


class BaseError(BaseModel):
    status: int = 500
    message: str = ""
    detail: str = ""


class Duplicated409(BaseError):
    status: int = 409
    message: str = "Duplicated record(s)"
