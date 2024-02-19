import os
import sys

from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from parse_sites import get_article_data
from database import get_connection

connection = get_connection()


url = "https://www.clarin.com/politica/gestiones-ultimo-minuto-gobierno-presento-nueva-propuesta-oposicion-dialoguista-tratar-salvar-ley-omnibus_0_U7oHzhhzJ6.html"
article_data = get_article_data(url)

with connection.cursor() as cursor:
    cursor.execute("SELECT url, id  FROM sources")
    result = cursor.fetchall()
    try:
        print(result[1])
        cursor.execute(
            "INSERT INTO scrap_articles (title, image, body, summary, authors, keywords, publish_date, source_id, created_at, updated_at, url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                article_data["title"],
                article_data["top_image"],
                article_data["body"],
                article_data["summary"],
                article_data["authors"],
                article_data["keywords"],
                article_data["publish_date"],
                result[1][1],
                datetime.now(),
                datetime.now(),
                article_data["url"],
            ),
        )
    except Exception as e:
        print("Error inserting data:", e)  # Add this line for debugging
    connection.commit()
