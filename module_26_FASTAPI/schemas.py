from pydantic import BaseModel
from datetime import time


class BaseMeal(BaseModel):
    name: str
    time_cook: time
    ingredients: str
    receipt_text: str


class BaseReceipt(BaseModel):
    name: str
    time_cook: time
    views: int

    class Config:
        orm_mode = True
