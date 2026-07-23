# Gunakan base image Python yang ringan
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Copy file requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua source code ke dalam container
COPY . .

# Beri tahu Docker bahwa aplikasi jalan di port 5003
EXPOSE 5003

# Perintah untuk menjalankan aplikasi saat container start
CMD ["python", "app.py"]