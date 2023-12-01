import streamlit as st
import pandas as pd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname='microservicegraph', user='admin', password='admin', host='database', port=5432)
cursor = conn.cursor()

st.title("Temperature Data Visualization")

login_id = st.text_input("Enter your ID:")
login_pw = st.text_input("Enter your Password:", type="password")

if login_id == "admin" and login_pw == "admin":
    st.success("Logged in successfully!")
    st.header("Temperature Graph")

    # Retrieve data from the 'temperature_data' table
    query = "SELECT * FROM temperature_data;"
    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["timestamp", "temperature"])

    st.write(df)

    st.line_chart(df.set_index("timestamp"))
else:
    st.warning("Incorrect ID or Password. Please try again.")

# Close the database connection
cursor.close()
conn.close()
