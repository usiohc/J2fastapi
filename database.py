from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
"""
from sqlalchemy.ext.declarative import declarative_base와 
from sqlalchemy.orm import declarative_base는 사실 같은 declarative_base 클래스를 가져옵니다. 
다만, 모듈의 구조가 다르기 때문에 이 두 가지 방식 중 하나를 선택하여 사용할 수 있습니다.

declarative_base 클래스가 sqlalchemy.ext.declarative 모듈에 정의되어 있습니다.
일반적으로는 sqlalchemy.ext.declarative 모듈을 사용하는 것이 ORM과 관련된 확장 기능을 더 많이 활용할 수 있기 때문에 선호되는 방식
"""
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL: str = "sqlite:///./myapi.db"

"""
create_engine, sessionmaker 등을 사용하는것은 SQLAlchemy 데이터베이스를 사용하기 위해 따라야 할 규칙

create_engine은 컨넥션 풀을 생성한다. 컨넥션 풀이란 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것
-> 컨넥션 풀은 데이터 베이스에 접속하는 세션수를 제어하고, 또 세션 접속에 소요되는 시간을 줄이고자 하는 용도로 사용

autocommit=True인 경우에는 commit이 필요없는 것처럼 rollback도 동작하지 않는다는 점
"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal은 데이터베이스에 접속하기 위해 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

# DI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
