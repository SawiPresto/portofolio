# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Menentukan direktori kerja dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstall dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000
# Menyalin seluruh isi proyek ke dalam container
COPY . .

# Menggunakan Gunicorn untuk menjalankan aplikasi
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
