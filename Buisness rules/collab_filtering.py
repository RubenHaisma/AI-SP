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

# This script will create a table with collaborative recommendations for each user
def collaborative_filtering():
    # Select all orders by the user
    order_sql = "SELECT productid FROM \"order\" WHERE sessionid IN (SELECT id FROM \"session\" WHERE profileid = %s)"
    cursor.execute(order_sql, (profile_id,))
    order_products = [p[0] for p in cursor.fetchall()]

    # Select all products viewed by the user
    viewed_sql = "SELECT productid FROM viewed_before WHERE profileid = %s"
    cursor.execute(viewed_sql, (profile_id,))
    viewed_products = [p[0] for p in cursor.fetchall()]

    # Select all products previously recommended to the user
    rec_sql = "SELECT productid FROM previously_recommended WHERE profileid = %s"
    cursor.execute(rec_sql, (profile_id,))
    rec_products = [p[0] for p in cursor.fetchall()]

    # Get recommendations for user
    recommend_sql = """SELECT r1.profileid, r1.productid, COUNT(*) AS frequency
                        FROM "order" r1
                        JOIN "order" r2 ON r1.sessionid = r2.sessionid AND r1.productid != r2.productid
                        WHERE r2.productid IN ({0}) AND r1.productid NOT IN ({0}, {1}, {2})
                        GROUP BY r1.profileid, r1.productid
                        ORDER BY frequency DESC"""
    cursor.execute(recommend_sql.format(','.join(str(p) for p in order_products),
                                        ','.join(str(p) for p in viewed_products),
                                        ','.join(str(p) for p in rec_products)))
    recommendations = cursor.fetchall()

    # Insert the recommendations into the collab_recommendations table
    if recommendations:
        for rec in recommendations:
            insert_sql = "INSERT INTO collab_recommendations (profileid, productid, frequency) VALUES (%s, %s, %s)"
            cursor.execute(insert_sql, (rec[0], rec[1], rec[2]))


def run():
    collaborative_filtering()
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    run()
