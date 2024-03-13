from pydantic import BaseModel
from datetime import datetime

class BaseMeal(BaseModel):
    name: str
    time_cook: datetime
    ingredients: str
    receipt_text: str


class BaseReceipt(BaseModel):
    name: str
    view: int
    time_cook: datetime


