"""GeoChangeAI backend entry point."""

from fastapi import FastAPI

app = FastAPI(title="GeoChangeAI API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
