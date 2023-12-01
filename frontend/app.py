import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(dbname='postgres', user='admin', password='admin', host='database', port=5432)
cursor = conn.cursor()

st.title("Temperature Data Visualization")

login_id = st.text_input("Enter your ID:")
login_pw = st.text_input("Enter your Password:", type="password")

if login_id == "admin" and login_pw == "admin":
    st.success("Logged in successfully!")
    st.header("Temperature Graph")
    query = "SELECT * FROM temperature_data;"
    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["timestamp", "temperature"])

    st.write(df)

    st.line_chart(df.set_index("timestamp"))
else:
    st.warning("Incorrect ID or Password. Please try again.")

cursor.close()
conn.close()
