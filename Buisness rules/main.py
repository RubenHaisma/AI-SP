import psycopg2
import dotenv

# load .env file
dotenv.load_dotenv()

def main():
    connection = psycopg2.connect(user="postgres",
                                password="postgres_password",
                                host="localhost",
                                port="5432",
                                database="postgres_DB")
    cursor = connection.cursor()
    with cursor as cursor:
        cursor.execute(open("recommendation/recommendation.sql", "r", encoding='utf-8').read())
    connection.commit()
    cursor.close()
    connection.close()