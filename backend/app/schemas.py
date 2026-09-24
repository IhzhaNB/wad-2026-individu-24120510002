from pydantic import BaseModel, Field


# Input — tidak ada id, karena id dibuat oleh server
class BukuCreate(BaseModel):
    judul: str
    penulis: str
    isbn: str = Field(pattern=r"^\d{13}$")
    tahun_terbit: int = Field(ge=1900, le=2026)
    harga: float = Field(gt=0)


# Output — ada id
class BukuOut(BukuCreate):
    id: int
