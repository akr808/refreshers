from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return("Hello")
@app.post("/req")
def req():
    return("Hello")

if __name__ == "__main__":
    app.run()