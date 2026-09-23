# ChatMe 🤖

ChatMe adalah backend REST API berbasis **FastAPI** untuk aplikasi chatbot. Berbeda dengan pendekatan chatbot RAG standar yang sangat bergantung pada Vector Database (seperti ChromaDB), ChatMe dirancang untuk menyimpan dan mengelola data pengguna, riwayat percakapan, dan logika bisnis menggunakan **Database Eksternal Relasional/NoSQL** (seperti PostgreSQL, MySQL, atau MongoDB).

Arsitektur proyek ini dibangun agar terukur (*scalable*), modular, dan siap untuk tahap *production*.

---

## ✨ Fitur Utama

- **FastAPI Framework**: Cepat, asinkron, dan mudah dikembangkan.
- **Database Tradisional**: Menggunakan database eksternal untuk menyimpan riwayat chat (*chat history*), profil pengguna, dan *state* percakapan (tanpa ketergantungan pada Vector DB).
- **Arsitektur Modular**: Pemisahan yang jelas antara *Router*, *Services*, *Schemas*, dan *Models*.
- **Auto-Generated Docs**: Dokumentasi API interaktif yang otomatis dibuat (Swagger UI & ReDoc).
- **Dependency Injection**: Pengelolaan koneksi database dan *security* yang efisien di setiap *endpoint*.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Server**: Uvicorn
- **ORM / Database Tool**: SQLAlchemy (Jika menggunakan SQL) atau Beanie/Motor (Jika menggunakan MongoDB)
- **Validasi Data**: Pydantic
- **Database**: PostgreSQL / MySQL (Silakan ubah sesuai database Anda)

---

## 📁 Struktur Direktori

Proyek ini menggunakan struktur standar *enterprise* untuk memastikan skalabilitas:

```text
chatme/
├── app/
│   ├── api/             # API Routers dan Dependencies
│   │   └── v1/          # Endpoints versi 1 (chat, users, dll)
│   ├── core/            # Konfigurasi aplikasi (config.py, security.py)
│   ├── db/              # Setup koneksi database dan engine
│   ├── models/          # Model Database (ORM)
│   ├── schemas/         # Skema Pydantic untuk request/response
│   ├── services/        # Logika bisnis chatbot dan manajemen data
│   └── main.py          # Entry point aplikasi FastAPI
├── .env.example         # Contoh file environment variables
├── requirements.txt     # Daftar dependensi Python
└── README.md