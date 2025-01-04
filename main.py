from fastapi import FastAPI

app=FastAPI()

@app.get("/") # The path is the root path and the method is GET
def root():
    return {"Hello":"World"} # When somebody visit "/", the function root() will be called and it will return a dictionary {"Hello":"World"}
