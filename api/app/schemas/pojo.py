from pydantic import BaseModel

class AddProductRequest(BaseModel):
    product_name:str
    price : float
    quantity :int

class AddDeviceRequest(BaseModel):
    name:str
    type:str
    property:dict
    aws_certificate:str
    aws_private_key:str
    aws_endpoint:str
       
    