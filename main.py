from itertools import count
from typing import Dict

from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field


class ItemPayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


class Item(ItemPayload):
    id: int


app = FastAPI(title="Local Items API", version="1.0.0")
items: Dict[int, Item] = {}
item_ids = count(1)


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemPayload) -> Item:
    item = Item(id=next(item_ids), **payload.dict())
    items[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int = Path(..., gt=0)) -> Item:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(
    payload: ItemPayload, item_id: int = Path(..., gt=0)
) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    item = Item(id=item_id, **payload.dict())
    items[item_id] = item
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int = Path(..., gt=0)) -> Dict[str, object]:
    if items.pop(item_id, None) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return {"id": item_id, "deleted": True}
