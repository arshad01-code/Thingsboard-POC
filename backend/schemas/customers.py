from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
