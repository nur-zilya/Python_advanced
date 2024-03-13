from sqlalchemy import Column, String, Integer, Time, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from datebase import Base

class Meal(Base):
    __tablename__ = 'Meal'
    meal_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    time_cook = Column(Time, index=True)
    ingredients = Column(String, index=True)
    receipt_text = Column(String, index=True)
    receipt_id = Column(Integer, ForeignKey('Receipts.id'), autoincrement=True)

    receipt = relationship('Receipts', back_populates="meals")


class Receipts(Base):
    __tablename__ = 'Receipts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    time_cook = Column(Time, index=True)
    views = Column(Integer, index=True, default=0)

    meals = relationship("Meal", back_populates="receipt")
