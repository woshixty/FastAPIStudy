from fastapi import FastAPI, Header, Body, Form

app = FastAPI()


# get param /?
@app.get("/param1/{id}")
def param1(id):
    return {"id": id}


# get param ?
@app.get("/param2")
def param2(id):
    return {"id": id}


# get header data
@app.get("/tokenGet")
def tokenGet(id, token=Header(None)):
    return {"id": id, "token": token}


# get body data
@app.post("/bodyGet")
def bodyGet(data=Body(None)):
    return {"data": data}


# get form data
@app.post("/formGet")
def formGet(username=Form(None), passwd=Form(None)):
    return {"data": {"username": username, "passwd": passwd}}

