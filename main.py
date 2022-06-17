from unicodedata import name
from fastapi import Depends, FastAPI, Request, Form, requests
#import jinja2
#from pydantic import BaseModel
from typing import Any, List
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.post("/login", response_class=HTMLResponse)
async def login(*, username:str=Form(...), password:str=Form(...)):

    
    return username
    


@app.get("/", response_class=HTMLResponse)
async def main(request:Request):
    return templates.TemplateResponse("form.html", context={"request":request})



@app.post("/submit", response_class=HTMLResponse)
def submit_file(*, request:Request, relate:str=Form(...),
                worries:str=Form(...),
                depends:str=Form(...),
                trust:str=Form(...),
                express:str=Form(...)):

    print(relate)
    htmlbody = f'''
    <h2>
    <p>relate:{relate}</p>
    <p>worries:{worries}</p>
    <p>depends:{depends}</p>
    <p>trust:{trust}</p>
    <p>express:{express}</p>
    <h2>
    '''
    return htmlbody
    #return templates.TemplateResponse("response.html", context={"request":request})