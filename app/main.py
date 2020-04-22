# coding: utf-8
from fastapi import FastAPI, Request, Body, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pprint
from db import db
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def survey(request: Request):
    return templates.TemplateResponse("encuesta.html", {"request": request})

@app.post("/")
def save_survey(*, request = Body(...)):
    surveys = db.surveys
    if surveys.insert_one(request):
        return True
    else:
        raise HTTPException(
            status_code=500,
            detail="Error al guardar datos de la encuesta",
        )
    

    
