from parse_sites import get_articles, get_article_data
from database import get_connection

connection = get_connection()

with connection.cursor() as cursor:
    cursor.execute("SELECT domain FROM Websites")
    result = cursor.fetchall()

    for domain in result:
        for article_url in get_articles(domain[0]):
            article_data = get_article_data(article_url)

            if article_data["title"] and article_data["body"]:
                try:
                    print(
                        "Inserting data:", article_data
                    )  # Add this line for debugging
                    cursor.execute(
                        "INSERT INTO Articles (title, top_image, publish_date, body, keywords, summary, url, authors) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            article_data["title"],
                            article_data["top_image"],
                            article_data["publish_date"],
                            article_data["body"],
                            article_data["keywords"],
                            article_data["summary"],
                            article_data["url"],
                            article_data["authors"],
                        ),
                    )
                except Exception as e:
                    print("Error inserting data:", e)  # Add this line for debugging
        connection.commit()
