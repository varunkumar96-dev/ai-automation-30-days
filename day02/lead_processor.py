import json
import getpass
import psycopg


# --------------------------------
# 1. Read JSON
# --------------------------------

with open("lead.json", "r") as file:
    lead = json.load(file)

print("Lead loaded:")
print(lead)


# --------------------------------
# 2. Validate required fields
# --------------------------------

required_fields = [
    "name",
    "email",
    "phone",
    "location",
    "requirement",
    "budget"
]

missing_fields = []

for field in required_fields:
    if field not in lead or not lead[field]:
        missing_fields.append(field)

if missing_fields:
    print("ERROR: Missing fields:", missing_fields)
    exit()


print("Validation successful!")


# --------------------------------
# 3. Get PostgreSQL password
# --------------------------------

password = getpass.getpass("Enter PostgreSQL password: ")


# --------------------------------
# 4. Connect to PostgreSQL
# --------------------------------

connection = psycopg.connect(
    host="localhost",
    port=5433,
    dbname="ai_automation",
    user="postgres",
    password=password
)


# --------------------------------
# 5. Check duplicate
# --------------------------------

with connection.cursor() as cursor:

    cursor.execute(
        """
        SELECT id
        FROM leads
        WHERE email = %s
        """,
        (lead["email"],)
    )

    existing_lead = cursor.fetchone()


# --------------------------------
# 6. Insert only if new
# --------------------------------

if existing_lead:

    print(
        f"Lead already exists with ID {existing_lead[0]}. "
        "Skipping insert."
    )

else:

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

    connection.commit()

    print("New lead inserted successfully!")


# --------------------------------
# 7. Close connection
# --------------------------------

connection.close()

print("Database connection closed.")