"""
import json
# Read the lead.json file
with open("lead.json", "r") as file:
    lead = json.load(file)

# Display the lead information
print("Customer Name:", lead["name"])
print("Email:", lead["email"])
print("Location:", lead["location"])
print("Requirement:", lead["requirement"])
print("Budget:", lead["budget"])
"""

import json
import getpass
import psycopg


# 1. Read lead.json
with open("lead.json", "r") as file:
    lead = json.load(file)

print("Lead loaded successfully!")
print("Name:", lead["name"])
print("Email:", lead["email"])


# 2. Ask for PostgreSQL password
password = getpass.getpass("Enter PostgreSQL password: ")


# 3. Connect to PostgreSQL
connection = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="ai_automation",
    user="postgres",
    password=password
)


# 4. Insert lead into PostgreSQL
with connection.cursor() as cursor:
    cursor.execute(
        """
        INSERT INTO leads
        (name, email, phone, location, requirement, budget)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            lead["name"],
            lead["email"],
            lead["phone"],
            lead["location"],
            lead["requirement"],
            lead["budget"]
        )
    )


# 5. Save the transaction
connection.commit()

# 6. Close connection
connection.close()

print("Lead inserted successfully into PostgreSQL!")
