FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

CMD python manage.py migrate && gunicorn food_engine.wsgi:application --bind 0.0.0.0:$PORT
