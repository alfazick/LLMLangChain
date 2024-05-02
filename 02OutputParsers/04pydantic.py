from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float 
    tags: list 


# Simulating a JSON response from an API
json_data = '{"name": "Widget", "price": 19.99, "tags": ["bestseller", "summer"]}'

product = Product.model_validate_json(json_data)

print(product)
