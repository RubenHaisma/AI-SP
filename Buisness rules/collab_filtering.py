import psycopg2
import pandas as pd

# connect to database
connection = psycopg2.connect(user="postgres",
                            password="postgres_password",
                            host="localhost",
                            port="5432",
                            database="huwebshop")
cur = connection.cursor() 

# Set profile_id to generate recommendations for
profile_id = "5a393d68ed295900010384ca"

# Get the products that have been recently restocked
cur.execute("SELECT id FROM product WHERE stock_level > 0 AND brand IN (SELECT brand FROM product WHERE id IN (SELECT productid FROM viewed_before WHERE profileid = %s) OR id IN (SELECT productid FROM previously_recommended WHERE profileid = %s)) ORDER BY stock_level DESC LIMIT 10;", (profile_id, profile_id))
recently_restocked_products = cur.fetchall()
recently_restocked_products = [product[0] for product in recently_restocked_products]

# Get the most frequently purchased products by the profile
cur.execute("SELECT productid, COUNT(*) AS count FROM \"order\" WHERE sessionid IN (SELECT id FROM \"session\" WHERE profileid = %s) GROUP BY productid ORDER BY count DESC LIMIT 10;", (profile_id,))
frequent_purchases = cur.fetchall()
frequent_purchases = [product[0] for product in frequent_purchases]

# Get the products that have been previously recommended to the profile
cur.execute("SELECT productid FROM previously_recommended WHERE profileid = %s LIMIT 10;", (profile_id,))
previously_recommended_products = cur.fetchall()
previously_recommended_products = [product[0] for product in previously_recommended_products]

# Get the products that the profile has viewed before
cur.execute("SELECT productid FROM viewed_before WHERE profileid = %s LIMIT 10;", (profile_id,))
viewed_products = cur.fetchall()
viewed_products = [product[0] for product in viewed_products]

# Combine all the product lists into a set of unique products
product_set = set(recently_restocked_products + frequent_purchases + previously_recommended_products + viewed_products)

# Create a dataframe of product attributes for the unique products
product_df = pd.read_sql_query("SELECT * FROM product WHERE id IN %s;", connection, params=(tuple(product_set),))

# Calculate a score for each product based on the profile's history and behavior
product_df['score'] = 0
for i, product in product_df.iterrows():
    if product['id'] in recently_restocked_products:
        product_df.at[i, 'score'] += 1
    if product['id'] in frequent_purchases:
        product_df.at[i, 'score'] += 2
    if product['id'] in previously_recommended_products:
        product_df.at[i, 'score'] += 3
    if product['id'] in viewed_products:
        product_df.at[i, 'score'] += 4

# Sort the products by score and get the top 4 recommendations
recommendations_df = product_df.sort_values('score', ascending=False).head(4)
recommendations = recommendations_df['id'].tolist()

# Print the recommendations
print("Top 4 recommended products for profile", profile_id, ":")
for i, recommendation in enumerate(recommendations):
    print(str(i+1) + ".", recommendation)

# Insert the recommendations into the database
for i, recommendation in enumerate(recommendations):
    cur.execute("INSERT INTO collab_recommendations (profileid, productid, score) VALUES (%s, %s, %s);", (profile_id, recommendation, i+1))

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()