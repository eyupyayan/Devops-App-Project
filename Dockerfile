FROM python:3.11-slim

# 1) Unngå at Python buffer output (bedre logging i container)
ENV PYTHONUNBUFFERED=1

# 2) Arbeidsmappe inni container
WORKDIR /app

# 3) Kopier requirements først (bedre cache: endrer kode ofte, deps sjeldnere)
COPY requirements.txt .

# 4) Installer dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5) Kopier app-koden
COPY app ./app

# 6) Appen lytter på 8000
EXPOSE 8000

# 7) Start server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
