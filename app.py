from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os

load_dotenv()

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=3306,
            user=os.getenv("DB_USER", "alx_client"),
            password=os.getenv("DB_PASSWORD", "alx_pass"),
            database=os.getenv("DB_NAME", "intro_db")
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def query_table(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 10")
        rows = cursor.fetchall()
        print(f"Data from {table_name}:")
        for row in rows:
            print(row)
        cursor.close()
    except Error as e:
        print(f"Error querying {table_name}: {e}")

def main():
    connection = connect_to_db()
    if connection:
        query_table(connection, "subscribers")
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
