import models
import asyncio
from datetime import time
from datebase import async_session


async def create_meal_with_receipt(meal_data, receipt_data):
    async with async_session() as db:
        db_meal = models.Meal(**meal_data)

        db_receipt = models.Receipts(**receipt_data)

        db_meal.receipt = db_receipt

        db_receipt.meals.append(db_meal)

        db.add(db_meal)
        db.add(db_receipt)
        await db.commit()

        return db_meal


async def main():
    time_str = "00:15:00"
    hour, minute, second = map(int, time_str.split(":"))
    time_obj = time(hour, minute, second)

    meal_data = {
        "name": "chicken carry",
        "time_cook": time_obj,
        "ingredients": "chicken, carry, rice",
        "receipt_text": "mix all ingredients"
    }

    receipt_data = {
        "name": meal_data["name"],
        "time_cook": meal_data["time_cook"],
        "views": 0
    }

    created_meal = await create_meal_with_receipt(meal_data, receipt_data)
    print(created_meal)

asyncio.run(main())
