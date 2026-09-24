# Tugas Individu — Endpoint Buku (FastAPI)

NIM: 24120510002

Endpoint sederhana untuk entitas **Buku**. Data disimpan di memori (belum pakai database).

## Prasyarat

- Python 3.11+
- Git

## Cara menjalankan

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Buka http://localhost:8000/docs untuk mencoba endpoint-nya.

## Endpoint

### POST /api/buku

Buat buku baru. Status **201** + header `Location`.

```json
{
  "judul": "Belajar Python",
  "penulis": "Budi",
  "isbn": "9781234567890",
  "tahun_terbit": 2020,
  "harga": 100000
}
```

Aturan validasi:

- `isbn` harus 13 digit angka
- `tahun_terbit` antara 1900 sampai 2026
- `harga` lebih dari 0

Kalau salah → status **422**.

### GET /api/buku

Ambil daftar buku. Status **200**.

Query: `?skip=0&limit=10&search=python`

### GET /api/buku/{id}

Ambil satu buku. Kalau tidak ada → status **404**.

## Cara memverifikasi

```bash
python verify.py --individu
```

Contoh coba manual di terminal:

```bash
# bikin buku (harus 201)
curl -i -X POST http://localhost:8000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul":"Belajar Python","penulis":"Budi","isbn":"9781234567890","tahun_terbit":2020,"harga":100000}'

# isbn salah (harus 422)
curl -i -X POST http://localhost:8000/api/buku \
  -H "Content-Type: application/json" \
  -d '{"judul":"X","penulis":"Y","isbn":"123","tahun_terbit":2020,"harga":1000}'

# id tidak ada (harus 404)
curl -i http://localhost:8000/api/buku/999
```

## Masalah yang sering muncul

| Masalah | Solusi |
|---|---|
| `ModuleNotFoundError: app` | jalankan uvicorn dari folder `backend/` |
| port 8000 bentrok | pakai `--port 8001` |
