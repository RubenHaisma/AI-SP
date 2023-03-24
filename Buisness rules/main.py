import psycopg2
import dotenv
import os

# Connectie maken met de database
conn = psycopg2.connect(
    database = os.getenv("postgres_DB"),
        host = 'localhost',
        port = '5432',
        password = os.getenv("postgres_password"),
        user = 'postgres'
)

# load env variables
dotenv.load_dotenv()

# Definiëren van logische regels voor aanbevelingen
def get_recommendations(profile_id):
    cursor = conn.cursor()
    cursor.execute("SELECT productid FROM previously_recommended WHERE profileid=%s", (profile_id,))
    previous_recommendations = cursor.fetchall()

    cursor.execute("SELECT productid FROM viewed_before WHERE profileid=%s", (profile_id,))
    previously_viewed = cursor.fetchall()

    cursor.execute("SELECT id FROM session WHERE profileid=%s", (profile_id,))
    sessions = cursor.fetchall()

    cursor.execute("SELECT id, brand, category, gender, sub_category, sub_sub_category, sub_sub_sub_category, price FROM product WHERE stock_level > 0 ORDER BY price DESC")
    products = cursor.fetchall()

    recommendations = []

    for product in products:
        if product['id'] not in previous_recommendations and product['id'] not in previously_viewed:
            for session in sessions:
                cursor.execute("SELECT productid FROM \"order\" WHERE sessionid=%s", (session,))
                session_orders = cursor.fetchall()
                if product['id'] in session_orders:
                    recommendations.append(product)
                    break
    return recommendations

# Voorbeeldgebruik van de get_recommendations functie
profile_id = '12345'
recommendations = get_recommendations(profile_id)
print(recommendations)

# Verbinding met de database verbreken
conn.close()
