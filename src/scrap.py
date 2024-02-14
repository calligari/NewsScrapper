from parse_sites import get_articles, get_article_data
import os
import pymysql.cursors
from dotenv import load_dotenv
import nltk

nltk.download("punkt")

load_dotenv()

db_host = os.getenv("DB_HOST") or "localhost"
db_user = os.getenv("DB_USER") or "root"
db_password = os.getenv("DB_PASSWORD") or ""
db_name = os.getenv("DB_NAME") or "test"

# Establecer la conexión a la base de datos
connection = pymysql.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    database=db_name,
)

with connection.cursor() as cursor:
    cursor.execute("SELECT domain FROM Websites")
    result = cursor.fetchall()

    for domain in result:
        for article_url in get_articles(domain[0]):
            article_data = get_article_data(article_url)
            print("Inserting data:", article_data)  # Add this line for debugging

            try:
                cursor.execute(
                    "INSERT INTO Articles (title, top_image, publish_date, body, keywords, summary, url) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        article_data["title"],
                        article_data["top_image"],
                        article_data["publish_date"],
                        article_data["body"],
                        "PLACEHOLDER",  ## article_data["keywords"],
                        "PLACEHOLDER",  ## article_data["summary"],
                        article_data["url"],
                    ),
                )
            except Exception as e:
                print("Error inserting data:", e)  # Add this line for debugging
        connection.commit()
