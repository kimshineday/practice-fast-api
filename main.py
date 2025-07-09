from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:  # 자료형 명시
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
