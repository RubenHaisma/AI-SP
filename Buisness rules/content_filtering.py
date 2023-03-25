import psycopg2
from dotenv import load_dotenv


# load .env file
load_dotenv()

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
    recommendList = []
    for product in similarProducts:
        print(product)
        if len(product) > 4 and product[4]: #category
            category = product[4]
            if len(product) > 3 and product[3]: #sub_category
                category = product[3]
                if len(product) > 2 and product[2]: #sub_sub_category
                    category = product[2]
                    recommendList.append(product[0])


        if len(recommendList) == 4:
            insertSql = f"""INSERT INTO content_recommendations 
                (category,product_recommendation)
                VALUES ('{category}')"""
            recommendList = []
            cursor.execute(insertSql)

def run():
    content_filtering()
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    run()
