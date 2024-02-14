from parse_sites import get_articles, get_article_data
from database import get_connection

connection = get_connection()

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
