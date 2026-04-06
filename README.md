# 📝 Praktikum Mahasiswa API — Live Blog

Replikasi Website Live Blog dengan Implementasi API menggunakan **FastAPI**, **SQLModel**, dan **PostgreSQL**.

> **Mata Kuliah:** Implementasi dan Pengembangan Basis Data (IPBD) — Praktikum  
> **NIM:** L0224042  
> **Kelas:** A

---

## 📋 Deskripsi

Aplikasi REST API untuk sistem blog sederhana yang memungkinkan mahasiswa untuk:

- **Register** — mendaftar sebagai pengguna baru (mendapatkan `access_token`)
- **CRUD Blog** — membuat, membaca, mengubah, dan menghapus postingan blog
- **Autentikasi** — menggunakan Bearer Token untuk endpoint yang membutuhkan otorisasi

---

## 🛠️ Tech Stack

| Komponen     | Teknologi                   |
| ------------ | --------------------------- |
| Framework    | FastAPI                     |
| ORM          | SQLModel (SQLAlchemy-based) |
| Database     | PostgreSQL 16               |
| Migration    | Alembic                     |
| Container    | Docker Compose              |
| Package Mgr  | Poetry                      |
| Python       | 3.10 – 3.11                 |

---

## 📁 Struktur Project

```
.
├── app/
│   ├── main.py              # Entry point aplikasi FastAPI
│   ├── helpers.py
│   ├── routes/
│   │   ├── blog.py          # Endpoint CRUD Blog
│   │   └── mahasiswa.py     # Endpoint Register Mahasiswa
│   └── services/
│       ├── blog_service.py      # Business logic Blog
│       └── mahasiswa_service.py # Business logic Mahasiswa
├── core/
│   └── config.py            # Konfigurasi aplikasi
├── db/
│   ├── init_db.py           # Inisialisasi database
│   └── session.py           # Koneksi & session database
├── models/
│   ├── blog.py              # Model tabel Blog
│   └── mahasiswa.py         # Model tabel Mahasiswa
├── schemas/
│   ├── blog.py              # Pydantic schema Blog
│   └── mahasiswa.py         # Pydantic schema Mahasiswa
├── utils/
│   └── auth.py              # Autentikasi Bearer Token
├── migrations/              # Alembic migration files
├── docker-compose.yaml      # Docker Compose untuk PostgreSQL
├── alembic.ini              # Konfigurasi Alembic
├── pyproject.toml           # Konfigurasi project & dependencies
└── README.md
```

---

## ⚙️ Prasyarat (Prerequisites)

Pastikan sudah terinstall di sistem Anda:

1. **Python 3.10 – 3.11**
2. **Poetry** (package manager) — [Cara install Poetry](https://python-poetry.org/docs/#installation)
3. **Docker & Docker Compose** — untuk menjalankan PostgreSQL

---

## 🚀 Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone <URL_REPOSITORY>
cd L0224042_A_HandsOn-1_IPDB
```

### 2. Install Dependencies

```bash
poetry install
```

### 3. Jalankan Database PostgreSQL (via Docker)

```bash
docker compose up -d
```

> Perintah ini akan menjalankan container PostgreSQL 16 dengan konfigurasi:
>
> | Parameter | Nilai                     |
> | --------- | ------------------------- |
> | Host      | `localhost`               |
> | Port      | `5436`                    |
> | User      | `postgres-ipbd`          |
> | Password  | `43210`                   |
> | Database  | `ipbd_db_tugasprak1`      |

Pastikan container sudah berjalan:

```bash
docker ps
```

### 4. Jalankan Database Migration (Alembic)

```bash
poetry run alembic upgrade head
```

### 5. Jalankan Aplikasi FastAPI

```bash
poetry run fastapi dev
```

Aplikasi akan berjalan di: **http://127.0.0.1:8000**

---

## 📖 Dokumentasi API

Setelah aplikasi berjalan, akses dokumentasi API interaktif di:

| Docs         | URL                                  |
| ------------ | ------------------------------------ |
| Swagger UI   | http://127.0.0.1:8000/docs          |
| ReDoc        | http://127.0.0.1:8000/redoc         |

---

## 🔗 Endpoint API

### Mahasiswa

| Method | Endpoint         | Deskripsi                  | Auth |
| ------ | ---------------- | -------------------------- | ---- |
| POST   | `/api/register`  | Register mahasiswa baru    | ❌   |

### Blog

| Method | Endpoint             | Deskripsi              | Auth |
| ------ | -------------------- | ---------------------- | ---- |
| POST   | `/api/blogs/`        | Buat blog baru         | ✅   |
| GET    | `/api/blogs/`        | Ambil semua blog       | ❌   |
| GET    | `/api/blogs/{id}`    | Ambil blog by ID       | ❌   |
| PUT    | `/api/blogs/{id}`    | Update blog            | ✅   |
| DELETE | `/api/blogs/{id}`    | Hapus blog             | ✅   |

### Utility

| Method | Endpoint   | Deskripsi        | Auth |
| ------ | ---------- | ---------------- | ---- |
| GET    | `/`        | Root message     | ❌   |
| GET    | `/health`  | Health check     | ❌   |

> **Auth ✅** = membutuhkan header `Authorization: Bearer <access_token>`  
> Token didapat saat register mahasiswa.

---

## 🔐 Contoh Penggunaan

### 1. Register Mahasiswa

```bash
curl -X POST http://127.0.0.1:8000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "nama": "Fatih Dzaki",
    "nim": "L0224042",
    "kelas": "A"
  }'
```

Response akan berisi `access_token` yang digunakan untuk autentikasi.

### 2. Buat Blog (dengan Token)

```bash
curl -X POST http://127.0.0.1:8000/api/blogs/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "judul": "Blog Pertama",
    "isi": "Ini adalah isi blog pertama saya."
  }'
```

### 3. Lihat Semua Blog

```bash
curl http://127.0.0.1:8000/api/blogs/
```

---

## 🛑 Menghentikan Project

```bash
# Hentikan aplikasi FastAPI
# Tekan Ctrl + C di terminal

# Hentikan container PostgreSQL
docker compose down
```

Untuk menghapus volume data database:

```bash
docker compose down -v
```

---

## 📌 Catatan Penting

- Pastikan **Docker** sudah berjalan sebelum menjalankan `docker compose up -d`
- Pastikan **database PostgreSQL** sudah aktif sebelum menjalankan aplikasi FastAPI
- Gunakan Python versi **3.10 – 3.11** (sesuai `pyproject.toml`)
