from fastapi import FastAPI

app = FastAPI()


@app.get("/foobar")
async def root():
    return {"message": "Hello World"}
