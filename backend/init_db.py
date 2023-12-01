import psycopg2
import random
from datetime import datetime, timedelta

default_db_params = {
    'dbname': 'postgres',
    'user': 'admin',
    'password': 'admin',
    'host': 'database',
    'port': 5432
}

conn = psycopg2.connect(
    dbname=default_db_params['dbname'],
    user=default_db_params['user'],
    password=default_db_params['password'],
    host=default_db_params['host'],
    port=default_db_params['port']
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS temperature_data (
        timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        temperature DOUBLE PRECISION
    );
""")

for _ in range(100):
    timestamp = datetime.utcnow() - timedelta(days=random.randint(0, 30))
    temperature = round(random.uniform(20.0, 30.0), 2)
    cursor.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (%s, %s);", (timestamp, temperature))

conn.commit()
cursor.close()
conn.close()

print("Database initialization completed successfully.")
