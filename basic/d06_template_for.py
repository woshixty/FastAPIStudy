from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("pages")
todos = ["write diary", "watch movie", "play game"]


# response html page
@app.get("/")
def templatePage1(req: Request):
    return template.TemplateResponse(
        "index.html", context={"request": req, "todos": todos}
    )


# get the_todo thing
@app.post("/addTodo")
def addTodo(todo=Form(None)):
    """ handle submit """
    todos.insert(0, todo)
    return RedirectResponse("/", status_code=302)
