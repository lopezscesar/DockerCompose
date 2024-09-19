from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    time.sleep(4)
    return {"item_id": item_id}
