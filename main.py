from typing import Union
from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
def read_root():
    #time.sleep(2 * 60)
    return {"Hello World"}