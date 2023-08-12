from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise

from dao.models import Todo

app = FastAPI()
template = Jinja2Templates("pages")

# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:123456@localhost:3306/fastapi1",
                  modules={'models': ['dao.models']},
                  add_exception_handlers=True,
                  generate_schemas=True)


# response html page
@app.get("/")
async def templatePage1(req: Request):
    # get data from database
    # ORM get all todos
    todos = await Todo.all()
    return template.TemplateResponse(
        "index.html", context={"request": req, "todos": todos}
    )


# get the_todo thing
@app.post("/addTodo")
async def addTodo(todo=Form(...)):
    """ handle submit """
    # todos.insert(0, t_todo)
    # insert new data to database
    await Todo(content1=todo).save()
    return RedirectResponse("/", status_code=302)


# SEARCH
@app.post("/search")
async def search(req: Request, keyword=Form(None)):
    # search keywords
    search_results = Todo.filter(content__icontains=keyword).all()
    return template.TemplateResponse("search_result.html",
                                     context={
                                         "request": req,
                                         "search_results": search_results,
                                     })
