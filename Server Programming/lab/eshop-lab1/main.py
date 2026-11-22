# Task - A2
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Server Programming, Jarif"}


# Task - B1
@app.get("/hello/{name}")
def get_hello(name: str):
    return {"message": f"Hello, {name}!"}



# Task - B2
@app.get("/square/{number}")
def get_square(number: int):
    return {"number": number, "square": number * number}



products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Mouse", "price": 800},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Monitor", "price": 12000},
    {"id": 5, "name": "Headphone", "price": 2500},
    {"id": 6, "name": "Smartphone", "price": 35000},
    {"id": 7, "name": "Tablet", "price": 22000},
    {"id": 8, "name": "Printer", "price": 9500},
    {"id": 9, "name": "Webcam", "price": 1800},
    {"id": 10, "name": "USB Drive", "price": 700},
]


### Task C1 & C2 has been added later due to "Path" complications ###



# Task - D1
from pydantic import BaseModel
class ProductCreate(BaseModel):
    name: str
    price: float



# Task - D2
@app.post("/addProduct")
def insert_product(product: ProductCreate):

    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)
    return new_product



# Task - E1
@app.get("/products/search")
def search_by_name(name: str):
    ans = []
    for product in products:
        if name.lower() in product["name"].lower():
            ans.append(product)

    return {"list": ans}



# Task - E2
@app.get("/products/affordable")
def filter_by_price(max_price: int):
    ans = []
    for product in products:
        if product["price"] <= max_price:
            ans.append(product)

    return {"list": ans}


# Task - C1
@app.get("/products")
def get_products():
    return {"list": products}


# Task - C2
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):

    for product in products:
        if product["id"] == product_id: 
            return product

    raise HTTPException(status_code=404, detail="Product not found")