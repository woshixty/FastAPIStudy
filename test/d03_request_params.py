from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/user/{id}")
def user(id):
    return {"id": id}



@app.get("/user2")
def user2(id):
    return {"id": id}


# get header data
@app.get("/user3")
def user3(id, token=Header(None)):
    return {"id": id, "token": token}


# get body data
@app.get("login")
def login():
