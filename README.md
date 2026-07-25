# TechNova Inventory API

REST API sederhana untuk manajemen inventory barang, dibangun dengan Flask. Project ini juga dilengkapi unit testing, containerization dengan Docker, serta CI/CD pipeline menggunakan GitHub Actions yang terintegrasi dengan SonarCloud untuk code quality dan test coverage.

## Fitur

- **GET /** — cek status API
- **GET /items** — ambil semua data inventory
- **POST /items** — tambah item baru ke inventory
- **GET /items/<id>** — ambil detail satu item berdasarkan ID
- **Monitoring** — metrics diekspos via Prometheus (`prometheus-flask-exporter`) untuk observability

## Tech Stack

- **Backend:** Python, Flask
- **Testing:** pytest / unittest (`test_app.py`)
- **Monitoring:** Prometheus Flask Exporter
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Code Quality:** SonarCloud (test coverage & static analysis)

## Cara Menjalankan

### Local (tanpa Docker)
```bash
pip install -r requirements.txt
python app.py
```
API akan berjalan di `http://localhost:5003`

### Dengan Docker
```bash
docker build -t technova-inventory .
docker run -p 5003:5003 technova-inventory
```

## Contoh Request

**Ambil semua item:**
```bash
curl http://localhost:5003/items
```

**Tambah item baru:**
```bash
curl -X POST http://localhost:5003/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Keyboard", "quantity": 20}'
```

## Menjalankan Test
```bash
pytest test_app.py
```

## Roadmap / Pengembangan Selanjutnya
- [ ] Ganti in-memory storage dengan database (PostgreSQL/SQLite)
- [ ] Tambah endpoint `PUT` dan `DELETE`
- [ ] Tambah validasi input & error handling yang lebih lengkap
- [ ] Tambah autentikasi (API key / JWT)
