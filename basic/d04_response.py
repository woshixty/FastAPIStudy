from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse

app = FastAPI()


@app.get("/responseCode")
def responseCode():
    return JSONResponse(content={"msg": "responseCode"},
                        status_code=203,
                        headers={"a": "b"})


# response html
@app.get("/htmlRes")
def htmlRes():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Colorful Hello World</title>
        <style>
            body {
                background-color: #333;
                color: white;
                text-align: center;
                padding-top: 200px;
                font-family: Arial, sans-serif;
            }
    
            h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }
    
            .rainbow-text {
                background-image: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <h1 class="rainbow-text">Hello, World!</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# response file
@app.get("/fileRes")
def fileRes():
    avatar = '../static/00672-2890830636.png'
    return FileResponse(path=avatar)
