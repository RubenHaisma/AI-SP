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
def content_recommendations():
    sql = """SELECT p.id,p.name,p.category,p.sub_category,p.sub_sub_category, COUNT (cart.product_id) AS WOW
            FROM product AS p
            FULL OUTER JOIN cart ON p.id = cart.product_id
            GROUP BY p.id,p.name,p.category,p.sub_category,p.sub_sub_category,cart.bought
            ORDER BY p.category,p.sub_category,p.sub_sub_category, COUNT(cart.product_id) DESC"""
    cursor.execute(sql)
    similarproduct = cursor.fetchall()
    recommendList = []
    for product in similarproduct:
        if product[4]: #category
            category = product[4]
            if product[3]: #sub_category
                category = product[3]
                if product[2]: #sub_sub_category
                    category = product[2]
                    recommendList.append(product[0])

        if len(recommendList) == 4:
            # String manipulation
            listString = str(recommendList).replace('[','{').replace(']','}').replace('\'','"')
            insertSql = f"""INSERT INTO content_recommendations 
                (category,product_recommendation)
                VALUES ('{category}','{listString}')"""
            recommendList = []
            cursor.execute(insertSql)

def collab_recommendations(segmentList,targetAudienceList):
    for segment in segmentList:
        for target in targetAudienceList:
            sql = f"""SELECT DISTINCT cart.product_id, cart.sessions_profiles_id, sessions.segment FROM cart
            INNER JOIN sessions ON cart.sessions_profiles_id = sessions.browser_id
            WHERE sessions.segment = '{segment}' 
            -- AND sessions.target_audience = '{target}'
            AND sessions.segment IS NOT NULL
            ORDER BY cart.product_id ASC"""
            cursor.execute(sql)
            allSimilarBuyersAndproduct = cursor.fetchall()
            used = []
            recommendList = []
            for buyerTypeAndProduct in allSimilarBuyersAndproduct:
                if buyerTypeAndProduct[0] in used:
                    continue
                else:
                    used.append(buyerTypeAndProduct[0])
                    recommendList.append(buyerTypeAndProduct[0])
                    if len(recommendList) == 4:
                        # String manipulation
                        listString = str(recommendList).replace('[','{').replace(']','}').replace('\'','"')
                        insertSql = f"""INSERT INTO collab_recommendations 
                            (segment,target_audience,product_recommendation)
                            VALUES ('{segment}','{target}','{listString}')"""
                        cursor.execute(insertSql)
                        recommendList = []

def run():
    content_recommendations()
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    run()
