from fastapi import FastAPI


app=FastAPI()

@app.get("/")
async def root():
    return {"Hello:World"}

@app.get("/user")
async def getUser():
    return {
        "id":1,
        "name":"Rifat",
        "email":"rifat@tikweb.com"
    }