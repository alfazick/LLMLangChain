# Example #2 Advanced Validations Using Validators

from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    username: str
    email: EmailStr

    @field_validator("email")
    def must_be_corporate_email(cls,value:str):
        allowed_domains = ["company.com", "company.org"]
        if value.split('@')[-1] not in allowed_domains:
            raise ValueError("Must use a corporate email address")
        return value 



try:
    user = User(username="john_doe", email = "john.doe@company.com")
    print(user)
except ValueError as e:
    print(e) 




