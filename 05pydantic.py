# Idea of Field from Pydantic

# Example #1 Validation: Using Field to enforce that a field adheres to specific constraints.
from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    price: float = Field(gt=0,
                         description="The price of the product must be greater than 0")
    

try:
    product = Product(price= -10.99)
except ValidationError as e:
    print(e)


# Example #2: Self-documentation: Using Field to provide a description

class User(BaseModel):
    age: int = Field(description="Age of the user in years")

#Printing model schema which includes field descriptions
print(User.model_json_schema())

# Example #3: Serialization and Metadata Management

class Item(BaseModel):
    name:str
    description: str = Field(alias='desc')

item = Item(name="Widget", desc="A useful tool")
print(item.model_dump_json())
