import psycopg2
from psycopg2 import sql
import random
from datetime import datetime, timedelta

db_params = {
    'dbname': 'microservicegraph',
    'user': 'admin',
    'password': 'admin',
    'host': 'database',
    'port': 5432
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname='postgres', user='admin', password='admin', host='database', port=5432)
conn.autocommit = True
cursor = conn.cursor()

# Create the role 'admin' with password 'admin' if it does not exist
cursor.execute(
    sql.SQL("DO $$ BEGIN IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = {role}) THEN "
            "CREATE ROLE {role} WITH LOGIN PASSWORD {password}; END IF; END $$;")
    .format(role=sql.Identifier('admin'), password=sql.Literal('admin'))
)

cursor.close()
conn.close()

# Connect to the PostgreSQL database with the specified user and password
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create the temperature_data table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS temperature_data (
        timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        temperature DOUBLE PRECISION
    );
""")

# Insert random data into the table
for _ in range(100):
    timestamp = datetime.utcnow() - timedelta(days=random.randint(0, 30))
    temperature = round(random.uniform(20.0, 30.0), 2)
    cursor.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (%s, %s);", (timestamp, temperature))

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Database initialization completed successfully.")
