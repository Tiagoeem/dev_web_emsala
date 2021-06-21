
# http://127.0.0.1:8000/docs
#uvicorn credit_score.main:app --reload

import json
from fastapi import FastAPI, Depends, Body
from fastapi import responses

from fastapi.responses import JSONResponse


app = FastAPI(title="Credit Score API",
    description="Api que retorna o score de pessoas para a mesa de crédito",
    version="0.3")
    

@app.get("/score/")
async def retorna_score():

    return {'mensagem': 987}
