from parse_sites import get_articles
import os
import pymysql.cursors
from dotenv import load_dotenv

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
        articles = get_articles(domain[0])
        print(articles)
