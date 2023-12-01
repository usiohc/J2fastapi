## [점프 투 FastAPI](https://wikidocs.net/175092)
#### [점프 투 FastAPI 소스 github](https://github.com/pahkey/fastapi-book) 

| stack     | version |
|-----------|---------|
| FastAPI   | 0.85.1  |
| Python    | 3.11.4  |
| NodeJS    | 18.16.0 |
| Svelte    | 3.49.0  |
| Bootstrap | 5.1.3   |



# Back

### FastAPI란?

#### 기존 프레임 워크와의 차이점 (유리한 점)
- react, Vue.js, Svelte와 같은 Frontend 웹 프레임워크에서 사용 가능
- 안드로이드, iOS, Flutter와 같은 모바일 앱 프레임워크에서 사용 가능

#### 속도가 빠름
- 파이썬 웹 프레임 워크중 가장 빠름
- Node.js, Go와 대등한 정도
    - FastAPI는 내부적으로 [Starlette](https://www.starlette.io/)라는 비동기 프레임워크를 사용해서임

#### 빠르게 작성 가능
- API 개발 순서는 다음과 같음
    1. 보통 입출력 스펙을 정함
    2. 기능 구현 후 테스트
- 입출력을 정의하고 입출력 값의 검증을 빠르고 안전하게 할 수 있음
    - [Pydantic](https://pydantic-docs.helpmanual.io/)
- 작성한 API는 자동으로 생성되는 API 문서를 통해 테스트 가능
    - [Swagger](https://swagger.io/)

#### DB
- 데이터베이스는 [SQLAlchemy](https://www.sqlalchemy.org)로 ORM을 사용


# Front

### Svelte
FastAPI로 만든 백엔드 서버에 데이터를 요청하고 응답을 받아서 처리하는 프로그램을 개발하기 위해서는 프론트엔드 프레임워크가 필요 -> Svelte

#### 장점
- Write less code
- No virtual DOM
    - React나 Vue.js와 같은 프레임워크는 가상돔을 사용하지만 Svelte는 가상돔을 사용하지 않음
    - 대신에 실제 Dom을 반영
    - Runtime에서 해석하지 않고 Buildtime 에서 Vanilla Javascript Bundle로 컴파일, 속도가 빠르고 라이브러리 배포할 필요가 없음
- Truly reactive


### 프론트엔드 서버(node.js)가 필요한 이유?
- Svelte로 작성한 코드를 실시간으로 테스트 해 보려면 Svelte로 작성한 코드를 브라우저가 인식할 수 있는 HTML, CSS, Javascript로 실시간 변환하는 기능이 필요
- Svelte로 작성한 코드를 빌드하면 순수 HTML과 CSS, Javascript가 만들어지므로 FastAPI 서버에 정적 파일 형태로 배포하면 됨
- 즉, 운영단계에서는 Node.js 서버가 필요없다.

<br>

## 프로젝트 구조

    ├── main.py
    ├── database.py
    ├── models.py
    ├── domain
    │   ├── answer
    │   ├── question
    │   └── user
    └── frontend

#### main.py
- app 객체를 통해 FastAPI의 설정을 함
    - 그렇다면 main.py는 FastAPI 프로젝트의 환경 설정을 하는 곳

#### database.py
- DB 관련 환경설정

#### models.py
- ORM을 사용하기 위해 SQLAlchemy를 사용, 모델 기반으로 DB 처리
- 모델 클래스를 정의

#### domain
- 해당 프로젝트는 질문과 답변을 작성하는 게시판을 만드는 것이 목적
    - 질문, 답변, 사용자 라는 3개의 도메인을 두어 관련한 파일을 작성


> - 질문 (question)
> - 답변 (answer)
> - 사용자 (user)

#### -> 각 도메인의 API를 생성 관리 하기위해서 다음과 같은 파일이 필요

- 라우트 파일 - URL과 API의 전체적인 동작을 관리
- 데이터베이스 처리 파일 - 데이터의 생성, 조회, 수정, 삭제 (CRUD) 를 처리
- 입출력 관리 파일 - 입력 데이터와 출력 데이터의 스펙 정의 및 검증

> - question_router.py - 라우터 파일
> - question_crud.py - 데이터베이스 처리 파일
> - question_schema.py - 입출력 관리 파일


#### frontend
- Svelte의 소스 및 빌드 파일들을 저장할 프론트엔드의 루트 디렉터리
- 최종적으로 frontend/dist 디렉터리에 생성된 빌드파일들을 배포시에 사용


<br>


### alembic

모델을 이용해 테이블 자동으로 생성

#### 초기화
```bash
alembic init migrations
```

- myapi 디렉터리 하위에 migrations라는 디렉터리와 alembic.ini 파일이 생성
-  migrations 디렉터리는 alembic 도구를 사용할 때 생성되는 리비전 파일들을 저장하는 용도로 사용
- alembic.ini 파일은 alembic의 환경설정 파일


#### 리비전 파일 생성
```bash
alembic revision --autogenerate
```


#### 리비전 파일 실행
```bash
alembic upgrade head
```

<br>

##### alembic 없이 테이블 생성하기
    main.py 파일에 다음의 문장을 삽입하면 FastAPI 실행시 테이블들이 모두 생성된다.

```python
import models
from database import engine
models.Base.metadata.create_all(bind=engine)
```

    매우 간단한 방법이지만 데이터베이스에 테이블이 존재하지 않을 경우에만 테이블을 생성
    한번 생성된 테이블에 대한 변경 관리를 할 수는 없음
    이러한 이유로 이 책에서는 이 방법을 사용하지 않고 alembic을 사용하여 데이터베이스를 관리

<br>

# 2-04 질문 목록 API

```bash
# FastAPI server
uvicorn main:app --reload

# Svelte server
npm run dev
```


### 라우터(Router)
- db.close() 함수는 사용한 세션을 컨넥션 풀에 반환하는 함수 (세션을 종료하는 것으로 착각하지 말자.)
    - db 세션 객체를 생성한 후에 db.close()를 수행하지 않으면 SQLAlchemy가 사용하는 컨넥션 풀에 db 세션이 반환되지 않아 문제가 생긴다
- 질문 목록 API인 question_list 함수에서 응답으로 모델 객체를 요소로 하는 리스트를 리턴하더라도 실제 리턴되는 값은 json 문자열로 자동 변환
    > serializer를 사용하지 않아도 자동으로 json으로 변환되는 건가?
    > -> FastAPI는 내부적으로 JSONResponse를 사용하여 자동으로 변환

    




<br>

### 의존성 주입(Dependency Injection)

- 위의 db.close()는 db에 접근할 때 마다 반복되는 패턴, 이를 자동화
    - [database.py](https://github.com/usiohc/J2fastapi/blob/master/database.py) 에 db 세션 객체를 리턴하는 제너레이터인 get_db 함수를 추가
    -  [제너레이터](https://wikidocs.net/134909) 함수에 [@contextlib.contextmanager 어노테이션](https://docs.python.org/ko/3/library/contextlib.html) 을 적용했으므로 다음과 같이 with 문과 함께 사용할 수 있다.

```python
@router.get("/list")
def question_list():
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
```
- with 문을 벗어나는 순간 get_db 함수의 finally에 작성한 db.close() 함수가 자동으로 실행
    1. with 문이 get_db() 함수의 try 블록에 진입
    2. yield가 실행되어 db 객체가 반환
    3. with 블록이 끝날 때까지 get_db 함수의 try 블록은 중단된 채로 대기
    4. with 블록이 끝나면 finally 블록이 실행되어 db.close()가 호출되어 데이터베이스 세션을 종료
    5. 커넥션 풀에 반환

### [Depends](https://fastapi.tiangolo.com/tutorial/dependencies/) 사용, with 보다 더 간단하게 사용
> 해당 내용외에도 매우 다양한 방법으로 활용 가능, 문서 참고

```python
@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
```
1. FastAPI의 Depends는 매개 변수로 전달 받은 함수를 실행시킨 결과를 리턴
2. get_db 함수를 with문과 함께 쓰는 대신에 question_list 함수의 매개변수로 db: Session = Depends(get_db) 객체를 주입
    > db: Session 타입 힌트를 사용해 db 객체가 Session 타입임을 명시
3. <b>get_db 함수에 자동으로 contextmanager가 적용</b>
    - Depends에서 contextmanager를 적용하게끔 설계되어 있다.
4. database.py의 get_db 함수는 다음과 같이 적용한 @contextlib.contextmanager 어노테이션을 제거
    - 제거하지 않으면 2중으로 적용되어 오류 발생

<br>

## Pydantic으로 하는 입출력 관리
Pydantic을 적용하기 위해서 가장 먼저 할 일은 질문 목록 API의 출력 스키마를 생성하는 것

- Pydantic은 데이터의 유효성 검사, 형 변환, 직렬화, 역직렬화 등을 자동으로 처리
    1. Request Validation (요청 유효성 검사)
    2. Data Serialization (데이터 직렬화)
    3. Response Validation (응답 유효성 검사)
- 아래 3가지 항목을 적용
    - 입출력 항목의 갯수와 타입을 설정
    - 입출력 항목의 필수값 체크
    - 입출력 항목의 데이터 검증


> BaseModel을 상속한 Question 클래스를 만들었음
> pydantic의 BaseModel을 상속한 Question 클래스를 앞으로 Question 스키마라고 정의
> - models.py 파일에 정의한 Question 클래스는 Question 모델



```python
import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
```
- Question 스키마에는 총 4개의 출력항목을 정의하고 그 타입을 지정했음 
- 정해진 타입이 아닌 다른 타입의 자료형이 대입되면 오류가 발생
- 4개 항목은 모두 디폴트 값이 없기 때문에 필수항목임을 나타낸다. 만약 subject 항목이 필수항목이 아니게 설정하려면 다음처럼 작성 (python 3.10 버전에서 추가된 type union)
```python
subject: str | None = None
# 변수명: 타입 or 타입 = 기본값
```
<br>

## 라우터에 Pydantic 적용시켜보기
```python
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
```

- question_list 함수의 @router.get 어노테이션에 response_model 속성을 추가
- 추가한 ``` response_model=list[question_schema.Question] ``` 의 의미는 question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미

> 만약 Question 스키마에서 content 항목을 제거한다면 질문 목록 API의 출력 항목에도 content 항목이 제거될 것     
> 이 때, 실제 리턴되는 _question_list를 수정할 필요가 없음
>> pydantic V1 을 사용하면 orm_mode 라는 issue가 존재 (최신 버전은 문제 X)


<br>

## CRUD 파일 작성

- 위에서 작성한 질문 목록 라우터 함수에는 데이터를 조회하는 다음의 부분이 포함되어 있음
```python
_question_list = db.query(Question).order_by(Question.create_date.desc()).all()
```
1. 라우터에 위와 같이 데이터를 조회하는 부분을 포함해도 문제는 없음
2. 다만, 데이터 처리하는 부분을 question_crud.py 파일에 분리하여 작성함
3. 서로 다른 라우터에서 데이터를 처리하는 부분이 동일하여 중복될 수 있음

<br>

```python
# [파일명: projects/myapi/domain/question/question_crud.py]
# - 질문 목록 라우터 함수에 있던 내용을 그대로 옮김

from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list




# [파일명: projects/myapi/domain/question/question_router.py]
# - get_question_list 함수를 사용할 수 있도록 질문 목록 라우터 함수를 수정
@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    return _question_list
```




<details>
<summary></summary>

비동기 방식의 질문 목록 조회

>FastAPI의 API 함수는 비동기 함수로 만들어 사용할수 있다. 다만, 이 책의 모든 예제는 설명의 편의상 비동기 방식이 아닌 동기 방식을 사용한다.      
왜냐하면 비동기 방식으로 모든 예제를 만들어 설명하는 것은 "FastAPI 공부" 라는 주 목적에 적합하지 않기 때문이다.     
(비동기 방식으로 코드를 만들면 코드의 양이 많아지고 가독성도 떨어진다.)

>비동기 방식의 API 함수를 만드는 방법에 대해서는 다음 부록을 참고하자.
> - 부록 - 비동기 방식으로 질문 목록 조회하기 : https://wikidocs.net/177352         

> 모든 API가 비동기로 구현된 파이보는 다음 URL에서 확인할 수 있다.
> - https://github.com/pahkey/fastapi-book/tree/async

</details>





