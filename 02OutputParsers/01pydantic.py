# Basic Data Validation

# Example #1

from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    name:str 
    age:int 

try:
    person = Person(name="Alice", age=30)
    print(person)
except ValidationError as e:
    print(e)


class User(BaseModel):
    name:str 
    age:int
    email:str 

# user_data = {
#     "name": "Tester1",
#     "age": "Eighteen", # wrong 
#     "email": "Tester1@example.com",
# }

user_data = {
    "name": "Tester1",
    "age": 18, #updated value
    "email": "Tester1@example.com",
}


user = User.model_validate(user_data)


print(user.name)
print(user.age)
print(user.email)