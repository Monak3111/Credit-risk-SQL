import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="09098072756",
    database="credit_risk_db"
)

cursor = conn.cursor()

print("Connected Successfully")