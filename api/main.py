import uvicorn
# from v1.app import app


if __name__ == "__main__":
    uvicorn.run("v1.app:app", reload=True)
