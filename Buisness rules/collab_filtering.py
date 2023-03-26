import psycopg2
from collections import Counter

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="huwebshop",
    user="postgres",
    password="1234"
)

# Prompt the user to enter a profile ID
profile_id = input("Enter a profile ID: ")

# Extract necessary data from the database
cursor = conn.cursor()
cursor.execute("""
    SELECT productid
    FROM viewed_before
    WHERE profileid = %s
""", (profile_id,))
data = cursor.fetchall()
cursor.close()

# Compute product frequency scores
product_scores = Counter()
for row in data:
    product_id = row[0]
    cursor = conn.cursor()
    cursor.execute("""
        SELECT profileid
        FROM viewed_before
        WHERE productid = %s
    """, (product_id,))
    profiles = cursor.fetchall()
    cursor.close()
    for profile in profiles:
        if profile[0] != profile_id:
            product_scores[product_id] += 1

# Close the database connection
conn.close()

# Print top recommended products
recommendations = [product_id for product_id, _ in product_scores.most_common(4)]
print("Top recommended products:")
for product_id in recommendations:
    print(product_id)
