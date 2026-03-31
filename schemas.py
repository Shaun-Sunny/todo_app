from pydantic import BaseModel


class todoBase(BaseModel):
    title: str
    status: bool = False


class todoCreate(todoBase):
    pass


class todoUpdate(todoBase):
    pass


class todoOut(todoBase):
    id: int

    class Config:
        from_attributes = True
