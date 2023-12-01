FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir psycopg2-binary

CMD ["bash", "-c", "python init_db.py && tail -f /dev/null"]

