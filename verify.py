#!/usr/bin/env python3
"""Cek tugas individu: python verify.py --individu"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def baca(*bagian):
    path = os.path.join(ROOT, *bagian)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--individu", action="store_true")
    args = ap.parse_args()
    if not args.individu:
        ap.error("pakai --individu")

    gagal = 0

    def cek(ok, label, catatan=""):
        nonlocal gagal
        if ok:
            print(f"  [OK  ] {label}")
        else:
            gagal += 1
            print(f"  [GAGAL] {label}" + (f" — {catatan}" if catatan else ""))

    main_py = baca("backend", "app", "main.py") or ""
    skema = baca("backend", "app", "schemas.py") or ""
    readme = (baca("README.md") or "").lower()

    cek(os.path.isfile(os.path.join(ROOT, "README.md")), "README.md ada")
    cek("fastapi" in main_py, "pakai FastAPI")
    cek('"/health"' in main_py, "ada rute /health")
    cek(
        os.path.isfile(os.path.join(ROOT, "backend", "requirements.txt")),
        "requirements.txt ada",
    )
    cek("BukuCreate" in skema and "BukuOut" in skema, "skema input dan output terpisah")
    cek(r"\d{13}" in skema, "isbn harus 13 digit")
    cek("ge=1900" in skema and "le=2026" in skema, "tahun_terbit 1900-2026")
    cek("HTTP_201_CREATED" in main_py or "201" in main_py, "POST memakai 201")
    cek("Location" in main_py, "POST set header Location")
    cek(all(p in main_py for p in ("skip", "limit", "search")), "GET list ada skip/limit/search")
    cek("404" in main_py, "GET by id bisa 404")
    cek("endpoint" in readme or "/api/buku" in readme, "README menjelaskan endpoint")

    print()
    if gagal:
        print(f"  {gagal} gagal. Perbaiki dulu.\n")
        return 1
    print("  Semua pemeriksaan lulus (PASS).\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
