from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_text():
    return "Hello there"
