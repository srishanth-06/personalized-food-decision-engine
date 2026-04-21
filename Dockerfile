FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["sh", "-c", "python manage.py migrate --noinput || true && gunicorn food_engine.wsgi:application --bind 0.0.0.0:$PORT"]
