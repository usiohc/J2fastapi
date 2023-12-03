import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime


    class Config:
        orm_mode = True
        # 2-04-4_질문목록API.md 참고 (pydantic V1 Issue)
