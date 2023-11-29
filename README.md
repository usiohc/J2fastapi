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