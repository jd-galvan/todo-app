from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

app = FastAPI()

@component
def App():
    return html.h1("Hola mundo")

configure(app, App)
