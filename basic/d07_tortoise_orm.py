from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()
template = Jinja2Templates("pages")
todos = ["write diary", "watch movie", "play game"]

# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:123456@localhost:3306/fastapi1",
                  modules={"models":[]},
                  add_exception_handlers=True,
                  generate_schemas=True)


# response html page
@app.get("/")
def templatePage1(req: Request):
    # get data from database
    # ORM
    return template.TemplateResponse(
        "index.html", context={"request": req, "todos": todos}
    )


# get the_todo thing
@app.post("/addTodo")
def addTodo(todo=Form(None)):
    """ handle submit """
    todos.insert(0, todo)
    # insert new data to database
    return RedirectResponse("/", status_code=302)
