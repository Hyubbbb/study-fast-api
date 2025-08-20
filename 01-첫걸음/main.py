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