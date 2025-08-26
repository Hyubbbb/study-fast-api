from fastapi import FastAPI

app = FastAPI() # FastAPI 인스턴스 생성


@app.get("/") # @로 시작하는 거: decorator
async def root(): # async: 비동기 함수 / async 대신 def 써도 됨 (동기)
    return {"message": "안녕하세요"}
"""
uvicorn main:app 명령은 다음을 의미합니다:

1. main: 파일 main.py (파이썬 "모듈").
2. app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
3. --reload: 코드 변경 시 자동으로 서버 재시작. 개발 시에만 사용.
"""

# [경로 매개변수]
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

## 순서 문제
"""
/users/me처럼, 현재 사용자의 데이터를 가져온다고 합시다.

사용자 ID를 이용해 특정 사용자의 정보를 가져오는 경로 /users/{user_id}도 있습니다.

경로 작동은 순차적으로 실행되기 때문에 /users/{user_id} 이전에 /users/me를 먼저 선언해야 합니다:
-> 순서를 반대로 하면, /users/me 요청 또한 매개변수 user_id의 값이 "me"인 것으로 "생각하게" 됩니다.
"""
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

## 사전정의 값 (Enum 클래스)
### Enum 클래스 사용
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}