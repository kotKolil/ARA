#external classes
from fastapi import *
from fastapi.responses import *
from sqlalchemy.orm import *
from sqlalchemy import *
from os import *

#importing local classes
from database import *

#creating object of web app
app = FastAPI()

#serving request to index page
@app.get("/")
def index(request:Request):
    return HTMLResponse("<H3>It works!</H3>")

#endpoints to get information about product with search with params
@app.get("/things")
def get(request:Request, Id = 0, name="null", customer = "null"):
    if Id:
        data = db.get(Product, Id)
        if data:
            return JSONResponse({"id":data.id, "name":data.name, "price":data.price, "customer":data.customer}, status_code=200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
    else:
        data = db.get(Product, id=Id, name=name, customer = customer)
        data = data.__dict__
        data.pop('_sa_instance_state', None)
        if data:
            return JSONResponse(data, status_code=200)
        else:
            return JSONResponse(["Not Found"], status_code=404)
        

@app.post("/things")
async def create(request:Request):
    data = await request.json()
    NewProduct = Product(id=data["id"], name=data["name"], customer=data["customer"], price = data["price"])
    db.add(NewProduct)
    db.commit()
    return JSONResponse(["Created"], status_code=201)

    

@app.patch("/things")
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
    

@app.delete("/things")
async def delete_product(request: Request,):
    data = await request.json()
    product_id = data.get("id")

    if product_id is None:
        return JSONResponse({"detail": "Missing product ID"}, status_code=400)

    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return JSONResponse({"message": "deleted"}, status_code=200)
    else:
        return JSONResponse({"detail": "Product not found"}, status_code=404)