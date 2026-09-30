FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

COPY . .

RUN pip install --no-cache-dir Flask==2.2.5

EXPOSE 5000

CMD ["python", "app.py"]
