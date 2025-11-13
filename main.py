from typing import Optional, Dict, Any
from fastapi import FastAPI
import time
from pydantic import BaseModel

class Item(BaseModel):
    idCallback: str
    idDatabase: str
    idCampaignAction: str
    cpf: str

class ItemResponse(BaseModel):
    def __str__(self):
        return f"ItemResponse(idCallback={self.idCallback})"

    idCallback: str
    idDatabase: str
    idCampaignAction: str
    answer: Optional[Dict[str, str]]

app = FastAPI()

@app.get("/")
def read_root():
    #time.sleep(2 * 60)
    return {"Hello World"}


@app.get("/link")
def retorna_link():
    time.sleep(2 * 60)
    return {"link": "https://colmeia.cx/"}

@app.post("/ehalt")
def recebe_ehalt(item: Item):
    time.sleep(1 * 60)
    item_response = ItemResponse(
        idCallback=item.idCallback,
        idDatabase=item.idDatabase,
        idCampaignAction=item.idCampaignAction,
        answer={"link": "https://colmeia.cx/"}
    )
    print(item_response)
    return item_response

