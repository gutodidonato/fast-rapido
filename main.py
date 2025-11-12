from typing import Optional, Dict, Any
from fastapi import FastAPI
import time
from pydantic import BaseModel

class Item(BaseModel):
    idCallBack: str
    idDataBase: str
    idCampaignAction: str
    cpf: str

class ItemResponse(BaseModel):
    idCallBack: str
    idDataBase: str
    idCampaignAction: str
    Optional[Dict[str, Any]]



app = FastAPI()


@app.get("/")
def read_root():
    #time.sleep(2 * 60)
    return {"Hello World"}


@app.get("/link")
def retorna_link():
    time.sleep(2 * 60)
    return {"link": "https://luishtml.com/"}

@app.post("/ehalt")
def recebe_ehalt(item: Item):
    time.sleep(2 * 60)
    item_response = ItemResponse(
        idCallBack=item.idCallBack,
        idDataBase=item.idDataBase,
        idCampaignAction=item.idCampaignAction,
        answer={"link": "https://luishtml.com/"}
    )
    return item_response
