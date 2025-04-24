from fastapi import FastAPI
import pyjokes
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Joke(BaseModel):
    friend: str
    joke: str


class JokeInput(BaseModel):
    friend: str

@app.get("/")
def joke():
    return pyjokes.get_joke()


@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())



@app.get("/{friend}")
def friends_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()


@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)