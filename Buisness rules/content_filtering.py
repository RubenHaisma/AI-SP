import psycopg2
import psycopg2.extensions
from dotenv import load_dotenv

# load .env file
load_dotenv()

# user-specific information
profile_id = input("Enter profile id: ") #5a393d68ed295900010384ca

# connect to database
connection = psycopg2.connect(user="postgres",
                            password="postgres_password",
                            host="localhost",
                            port="5432",
                            database="huwebshop")
cursor = connection.cursor()

# This script will create a table with content recommendations for each category
def collaborative_filtering():
    viewed_sql = f"SELECT productid FROM viewed_before WHERE profileid='{profile_id}'"
    cursor.execute(viewed_sql)
    viewed_products = [str(p[0]) for p in cursor.fetchall()]

    purchased_sql = f"SELECT productid FROM \"order\" WHERE sessionid IN (SELECT id FROM \"session\" WHERE profileid='{profile_id}')"
    cursor.execute(purchased_sql)
    purchased_products = [str(p[0]) for p in cursor.fetchall()]

    recommendations = list(set(viewed_products + purchased_products))

    # Insert the recommendations into the previously_recommended table
    if recommendations:
        for r in recommendations:
            insert_sql = "INSERT INTO previously_recommended (profileid, productid) VALUES (%s, %s) ON CONFLICT DO NOTHING"
            cursor.execute(insert_sql, (profile_id, r))

    # Get the recommendations from previously_recommended table
    select_sql = f"SELECT productid FROM previously_recommended WHERE profileid='{profile_id}'"
    cursor.execute(select_sql)
    recommendations = [str(p[0]) for p in cursor.fetchall()]

    # Insert the recommendations into the previously_recommended table
    if recommendations:
        for r in recommendations:
            insert_sql = "INSERT INTO previously_recommended (profileid, productid) VALUES (%s, %s) ON CONFLICT DO NOTHING"
            cursor.execute(insert_sql, (profile_id, r))

    # Insert the recommendations into the content_recommendations table
    if recommendations:
        for r in recommendations:
            select_sql = f"SELECT category, sub_category, sub_sub_category FROM product WHERE id='{r}'"
            cursor.execute(select_sql)
            category = cursor.fetchone()
            if category:
                insert_sql = "INSERT INTO collab_recommendations (profile_id, product_id, category, product_recommendation) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING"
                cursor.execute(insert_sql, (profile_id, r, category[0], str(recommendations)))

def run():
    collaborative_filtering()
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    run()
