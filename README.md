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

# 2장 개발 기초 공사

### [2-03_개발환경세팅](docs\2-03_개발환경세팅.md)
### [2-04_질문목록API](docs\2-04-4_질문목록API.md)
### [2-05_질문목록화면](docs\2-05-3_질문목록화면.md)
### [2-06_질문상세](docs\2-06_질문상세.md)
### [2-07_답변등록](docs\2-07_질문상세.md)
### [2-08_화면예쁘게꾸미기](docs\2-08_화면예쁘게꾸미기.md)
### [2-09_부트스트랩](docs\2-09_부트스트랩.md)
### [2-10_질문등록API](docs\2-10_질문등록API.md)

<br>

# 3장 파이보 서비스 개발
이 장의 목표
- 파이보를 상용 게시판 수준으로 본격적으로 개발한다.
- 부트스트랩을 적용하여 서비스를 더 아름답게 만든다.
- 게시물 등록, 삭제, 수정부터 로그인, 로그아웃, 페이징, 검색까지 게시판을 완벽하게 만든다.

### [3-01_내비게이션바](docs\3-01_내비게이션바.md)
### [3-02_게시판페이징](docs\3-02_게시판페이징.md)
### [3-03_스토어](docs\3-03_스토어.md)
### [3-04_날짜표시하기](docs\3-04_날짜표시하기.md)
### [3-05_게시물일련번호](docs\3-05_게시물일련번호.md)
### [3-06_답변개수표시](docs\3-06_답변개수표시.md)
### [3-07_회원가입](docs\3-07_회원가입.md)
### [3-08_로그인_로그아웃](docs\3-08_로그인_로그아웃.md)
### [3-09_글쓴이저장](docs\3-09_글쓴이저장.md)
### [3-10_글쓴이표시](docs\3-10_글쓴이표시.md)