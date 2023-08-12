from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
template = Jinja2Templates("pages")


# response html page
@app.get("/")
def templatePage1(username, req: Request):
    return template.TemplateResponse(
        "index.html", context={"request": req, "name": username}
    )
