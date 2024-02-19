from parse_sites import get_articles, get_article_data
from datetime import datetime
from database import get_connection

connection = get_connection()

with connection.cursor() as cursor:
    cursor.execute("SELECT url, id  FROM sources")
    result = cursor.fetchall()

    for domain, id in result:
        for article_url in get_articles(domain):
            try:
                article_data = get_article_data(article_url)

                if article_data["title"] and article_data["body"]:
                    try:
                        print(article_data["title"])
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
                                id,
                                datetime.now(),
                                datetime.now(),
                                article_data["url"],
                            ),
                        )
                    except Exception as e:
                        print("Error inserting data:", e)  # Add this line for debugging
            except Exception as e:
                print("Error parsing article:", e)

        connection.commit()
