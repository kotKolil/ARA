#external classes
from fastapi import *
from fastapi.responses import *
from sqlalchemy.orm import *
from sqlalchemy import *

#importing local classes
from database import *

#creating object of web app
app = FastAPI()

#serving request to index page
@app.get("/")
def index(request:Request):
    return HTMLResponse("<H3>It works!</H3>")

#endpoints to get information about product with search with params
@app.get("/get")
def get(request:Request, Id = 0, name="null", customer = "null"):
    if Id:
        data = db.get(Product, Id)
        if data:
            return JSONResponse(data, status_code=200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
    else:
        data = db.get(Product, id=Id, name=name, customer = customer)
        if data:
            return JSONResponse(data, status_code=200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
        

@app.post("/create")
async def create(request:Request):
    try:
        data = await request.json()
        NewProduct = Product(id=data["id"], name=data["name"], customer=["customer"], price = data["price"])
        db.add(NewProduct)
        db.commit()
        return JSONResponse(["Created"], status_code=201)
    except Exception as e:
        return JSONResponse([str(e)], status_code=500)
    

@app.post("/update")
async def update(request:Request):
    data = await request.json()
    try:
        product = db.query(Product).filter(Product.id == data["id"]).first()
        if (product):
            product.name = data["name"]
            product.customer = data["customer"]
            product.price = data["price"]
            db.commit()
            return JSONResponse(["Updated"], status_code=200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
    except Exception as e:
        return JSONResponse([str(e)], status_code=500)
    

@app.delete("/delete")
async def dlt(request:Request):
    try:
        data = await request.data()
        product = db.query(Product).filter(Product.id == data["id"]).first()
        if product:
            db.delete(product)
            db.commit()
            return JSONResponse(["deleted"], status_code= 200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
    except Exception as e:
        return JSONResponse([str(e)], status_code=500)