from fastapi import FastAPI
from sqlalchemy.future import select

import models
import schemas
from datebase import session, engine

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/receipts", response_model=list[schemas.BaseReceipt])
async def show_receipts() -> list[schemas.BaseReceipt]:
    db_receipts = await session.execute(
        select(models.Receipts).order_by(models.Receipts.views.desc(), models.Receipts.time_cook)
    )
    return [schemas.BaseReceipt.from_orm(db_receipt) for db_receipt in db_receipts.scalars()]


@app.get("/receipts/{receipt_id}", response_model=schemas.BaseReceipt)
async def view_receipt(receipt_id: int):
    # Извлекаем рецепт из базы данных
    db_receipt = await session.execute(select(models.Receipts).filter(models.Receipts.id == receipt_id))
    db_receipt = db_receipt.scalar_one_or_none()

    if db_receipt:
        # Увеличиваем количество просмотров рецепта
        db_receipt.views += 1
        await session.commit()
        return schemas.BaseReceipt.from_orm(db_receipt)
    else:
        # Если рецепт с указанным ID не найден, возвращаем ошибку или пустой ответ
        return {"detail": "Receipt not found"}
