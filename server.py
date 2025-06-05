from pages import index_page, md_page
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
        "*",
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


@app.get("/")
def index():
    return HTMLResponse(index_page())

@app.get("/{pagename}")
def page(pagename: str):
    res = md_page(pagename)
    if res:
        return HTMLResponse(res)
    return not_found()

def not_found():
    return HTMLResponse("<p>Page not found</p><br /><h1>404.</h1>")
