from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi import APIRouter

router  = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items = [
    Item(id=1, name="Item 1", description="This is item 1", price=10.0, tax=1.0),
    Item(id=2, name="Item 2", description="This is item 2", price=20.0, tax=2.0)
]

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item

@router.get("/items/", response_model=List[Item])
def read_items():
    return items

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")



