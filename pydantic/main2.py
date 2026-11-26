# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str                          # 필수
    description: Optional[str] = None  # 선택, 기본값 None
    price: float                       # 필수
    tax: float = 0.1                   # 선택, 기본값 0.1

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.model_dump()}

# 실행: uvicorn main:app --reload