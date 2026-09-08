from fastapi import FastAPI

from Backend.app.core.config import settings

app = FastAPI(title=settings.APP_NAME)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
