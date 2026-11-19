FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir --upgrade Flask Werkzeug Jinja2 SQLAlchemy Flask-SQLAlchemy Flask-Script Flask-Migrate

COPY . .

EXPOSE 7345

CMD ["python", "manage.py", "runserver", "--host=0.0.0.0", "--port=7345"]