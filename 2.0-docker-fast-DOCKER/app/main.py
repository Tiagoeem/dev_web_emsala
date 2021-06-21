import json
from fastapi import FastAPI, Depends, Body
from fastapi import responses
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/")
async def raiz():

    return {'mensagem': 'Ola Mundo'}


@app.get("/modelo/")
async def retorna_modelo():

    return {'resultado': 1}
