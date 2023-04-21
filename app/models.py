from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    line_user_id: str
    created_at: str
    updated_at: str


class DiaryTemplate(BaseModel):
    id: int
    template_name: str
    template_text: str
    created_at: str
    updated_at: str


class Payment(BaseModel):
    id: int
    user_id: int
    amount: float
    currency: str
    payment_method: str
    created_at: str
    updated_at: str
