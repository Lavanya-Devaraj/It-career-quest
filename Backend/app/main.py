from fastapi import FastAPI

app = FastAPI(title="IT Career Quest API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}
