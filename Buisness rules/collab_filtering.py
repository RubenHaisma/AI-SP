import psycopg2
from dotenv import load_dotenv

# load .env file
load_dotenv()

# Connect to the database
connection = psycopg2.connect(user="postgres",
                            password="postgres_password",
                            host="localhost",
                            port="5432",
                            database="huwebshop")
cursor = connection.cursor()
print ("Database opened successfully")

# Create a cursor
cur = connection.cursor()

# Get the list of all users
cur.execute("SELECT id FROM profile")
users = cur.fetchall()
print(f"Found {len(users)} users")

# Create a dictionary to store the products purchased by each user
user_products = {}
for user in users:
    user_products[user[0]] = set()
    cur.execute(
        "SELECT productid FROM \"order\" JOIN \"session\" ON \"order\".sessionid = \"session\".id WHERE profileid=%s",
        (user[0],)
    )
    results = cur.fetchall()
    for result in results:
        user_products[user[0]].add(result[0])
print ("Found products for all users")

# Compute the similarity between users based on the Jaccard similarity of their product sets
def jaccard_similarity(set1, set2):
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

# Get the most similar users to a given user
def get_similar_users(profile_id):
    similarities = {}
    for user in users:
        if user[0] == profile_id:
            continue
        similarity = jaccard_similarity(user_products[profile_id], user_products[user[0]])
        similarities[user[0]] = similarity
    return sorted(similarities, key=similarities.get, reverse=True)[:10]

# Get the products purchased by the most similar users that the given user has not already purchased
def get_recommendations(profile_id):
    similar_users = get_similar_users(profile_id)
    recommendations = set()
    for user in similar_users:
        cur.execute(
            "SELECT productid FROM \"order\" JOIN \"session\" ON \"order\".sessionid = \"session\".id WHERE profileid=%s AND productid NOT IN %s",
            (user, tuple(user_products[profile_id]))
        )
        results = cur.fetchall()
        for result in results:
            recommendations.add(result[0])
    return list(recommendations)[:4]

# Store the recommendations in the database
def store_recommendations(profile_id, recommendations):
    cur.execute("INSERT INTO recommendations (profileid, productid1, productid2, productid3, productid4) VALUES (%s, %s, %s, %s, %s)",
                (profile_id, recommendations[0], recommendations[1], recommendations[2], recommendations[3]))
    connection.commit()

# Example usage
profile_id = input("Enter profile id: ")
recommendations = get_recommendations(profile_id)
store_recommendations(profile_id, recommendations)

# Close the connection
cur.close()
connection.close()


