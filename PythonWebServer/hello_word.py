from fastapi import FastAPI,status
from fastapi.responses import JSONResponse # for json response
from switch_users import Role

app=FastAPI()

@app.get("/")
async def root():
    return {"Hello:World"}

# @app.get("/user") # user path 
# async def getUser():
#     return {
#         "id":1,
#         "name":"Rifat",
#         "email":"rifat@tikweb.com"
#     }
    
@app.get("/user")
async def user():
     return JSONResponse(status_code=status.HTTP_200_OK,content={"user":True})
 
# @app.get("/user/{id}")
# async def getUser(id:int):
    
#     if id<=0:
#         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"user":False})
    
#     return JSONResponse(status_code=status.HTTP_200_OK,content={"user":id}) 
 
@app.get("/user/{role}")
async def getRole(role:Role):
     
    if role is Role.ADMIN:
        return JSONResponse(status_code=status.HTTP_200_OK,content={"role":"admin"})

    return JSONResponse(status_code=status.HTTP_200_OK,content={"role":"user"})
