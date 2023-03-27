# The function content_filtering was created with the help of AI (ChatGPT 3)

import psycopg2
import psycopg2.extensions
from dotenv import load_dotenv

# load .env file
load_dotenv()

# user-specific information
profile_id = input("Enter profile id: ") #5a393d68ed295900010384ca
cart_products = input("Product ID's: ").split(',') #16121

# connect to database
connection = psycopg2.connect(user="postgres",
                            password="postgres_password",
                            host="localhost",
                            port="5432",
                            database="huwebshop")
cursor = connection.cursor() 

# This script will create a table with content recommendations for each category
def content_filtering():
    sql = """SELECT p.id,p.category,p.sub_category,p.sub_sub_category
            FROM product AS p
            GROUP BY p.id,p.category,p.sub_category,p.sub_sub_category
            ORDER BY p.category,p.sub_category,p.sub_sub_category"""
    cursor.execute(sql)
    similarProducts = cursor.fetchall()
    recommendDict = {}
    for product in similarProducts:
        # Determine the most specific category name that is present
        category = None
        if product[3]:
            category = product[3] # sub_sub_category
        elif product[2]:
            category = product[2] # sub_category
        elif product[1]:
            category = product[1] # category

        # Add the product name to the list of recommendations for the category
        if category and product[0]:
            if category not in recommendDict:
                recommendDict[category] = []
            recommendDict[category].append(str(product[0]))

    # Insert the recommendations into the content_recommendations table
    if recommendDict:
        for category, recommendations in recommendDict.items():
            values = ','.join([f"'{r}'" for r in recommendations]).replace(' ', '"')
            insertSql = "INSERT INTO content_recommendations (profile_id, product_id, category, product_recommendation) VALUES (%s, %s, %s, %s)"
            # recommend products based on user's cart
            if set(cart_products).intersection(set(recommendations)):
                cursor.execute(insertSql, (profile_id, product[0], category, recommendations))



def run():
    content_filtering()
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    run()
