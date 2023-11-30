from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text,nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    '''
    question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가
    sqlalchemy.orm.relationship으로 question 속성을 생성하면
    답변 객체(예: answer)에서 연결된 질문의 제목을 answer.question.subject 처럼 참조가능
    '''
