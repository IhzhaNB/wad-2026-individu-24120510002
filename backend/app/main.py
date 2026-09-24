from fastapi import FastAPI

app = FastAPI(title="Tugas Individu — Buku")


@app.get("/health")
def health():
    return {"status": "ok"}
