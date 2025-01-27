from fastapi import FastAPI,status
from fastapi.responses import JSONResponse # for json response

app=FastAPI()

@app.get("/")
async def index(q:str="empty"): # query parameter
    
    if q=="empty":
        return JSONResponse(status_code=status.HTTP_200_OK,content={"output":"Empty"})
    
    return JSONResponse(status_code=status.HTTP_200_OK,content={"output":q})

fake_items_db=[{"item_name":"foo"},{"item_name":"bar"},{"item_name":"baz"}]

@app.get("/items")
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]