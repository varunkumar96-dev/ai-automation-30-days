import getpass
import psycopg

password = getpass.getpass("Enter PostgreSQL password: ")

try:
    connection = psycopg.connect(
        host="localhost",
        port=5433,
        dbname="ai_automation",
        user="postgres",
        password=password
    )

    print("Successfully connected to PostgreSQL!")

    connection.close()

except Exception as error:
    print("Connection failed:")
    print(error)