from fastapi import FastAPI, Depends
from enum import Enum

app = FastAPI(name="FastAPI Depends example")

mar = {
    "name": "Mar",
    "profession": "HHRR",
    "likes_job": False,
}


gero = {
    "name": "Gero",
    "profession": "Programmer",
    "likes_job": True,
}

authorized_users = [
    "Gero",
]


class Messages(Enum):
    NonAuthorized: str = "Non Authorized"
    Authorized: str = "Authorized"


# Dependencia que sea simplemente chequear qué permisos se tiene
def check_user_permits(user_name: str):
    return user_name in authorized_users


@app.get("/")
def home():
    message = {
        "Mar": mar,
        "Gero": gero,
    }
    return message


@app.get("/authorized-content")
def authorized_content(user_name=Depends(check_user_permits)):
    if user_name:
        return Messages.Authorized
    return Messages.NonAuthorized
