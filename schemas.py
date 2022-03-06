from pydantic import BaseModel


class Repository(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
