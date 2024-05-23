from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from posts import Posts
import random
import string

app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hi": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


inputs = ['e', 'f', 'g', 'h']
weights = [10, 30, 50, 10]

def get_random_letter(inputs, weights):
    r = random.uniform(0, sum(weights))
    current_cutoff = 0
    for index in range(len(weights)):
        current_cutoff = current_cutoff + weights[index]
        if r < current_cutoff:
            return inputs[index]



@app.get("/post")
async def posts():
    return get_random_letter(inputs, weights)