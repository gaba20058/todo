FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7345

CMD ["sh", "-c", "python -c \"from application import create_app; from application.extensions import db; app = create_app(); app.app_context().push(); db.create_all()\" && python manage.py runserver --host=0.0.0.0 --port=7345"]