from pydantic import BaseModel
from typer import Option


class LoginModel(BaseModel):
    username: str
    password: str

class RegisterModel(BaseModel):
    id: int
    firs_name: str
    last_name: str
    email: str
    username: str
    password: str

class OrderModel(BaseModel):
    id: int
    product_id: int
    user_id: int
    count: int
    order_status: str

class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    count: int
    price: float

class CategoryModel(BaseModel):
    id: int
    name: str

class JWTModel(BaseModel):
    authjwt_secret_key: str = 'a3ea7202dcec5b0808438c4f782793243f479b9819267b8122598d630df57d80'

