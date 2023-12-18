FROM python:3.8-slim

# Install build tools and libpq-dev
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENV NAME World

CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
