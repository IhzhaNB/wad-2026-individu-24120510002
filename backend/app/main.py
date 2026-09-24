from fastapi import FastAPI, HTTPException, Query, Response
from fastapi import status

from app.schemas import BukuCreate, BukuOut

app = FastAPI(title="Tugas Individu — Buku")

# data sementara di memori
buku_list: list[dict] = []
next_id = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/buku", response_model=BukuOut, status_code=status.HTTP_201_CREATED)
def tambah_buku(payload: BukuCreate, response: Response):
    global next_id
    data = {"id": next_id, **payload.model_dump()}
    next_id += 1
    buku_list.append(data)
    response.headers["Location"] = f"/api/buku/{data['id']}"
    return data


@app.get("/api/buku", response_model=list[BukuOut])
def daftar_buku(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
):
    hasil = buku_list
    if search:
        q = search.lower()
        hasil = [
            b
            for b in hasil
            if q in b["judul"].lower() or q in b["penulis"].lower() or q in b["isbn"]
        ]
    return hasil[skip : skip + limit]


@app.get("/api/buku/{buku_id}", response_model=BukuOut)
def detail_buku(buku_id: int):
    for b in buku_list:
        if b["id"] == buku_id:
            return b
    raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
