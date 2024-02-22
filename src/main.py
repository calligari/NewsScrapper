from parse_sites import get_articles, get_article_data
from datetime import datetime
from database import get_connection
from newspaper import Source
from newspaper.mthreading import fetch_news
import threading

connection = get_connection()


class NewsCrawler:
    def __init__(self, source_urls, config=None):
        self.sources = [Source(url, config=config) for url in source_urls]
        self.articles = []

    def build_sources(self):
        # Multithreaded source building
        threads = [threading.Thread(target=source.build) for source in self.sources]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def crawl_articles(self):
        # Multithreaded article downloading
        self.articles = fetch_news(self.sources, threads=8)

    def extract_information(self):
        # Extract information from each article
        for source in self.sources:
            print(f"Source {source.url}")
            with connection.cursor() as cursor:
                cursor.execute("select id from sources where url=%s", source.url)
                id = cursor.fetchone()[0]
            print(id)
            for article in source.articles[:10]:
                article.parse()
                article.nlp()
                print(f"Title: {article.title}")
                print(f"Authors: {article.authors}")
                print(f"Text: {article.text[:150]}...")
                print("-------------------------------")
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO scrap_articles (title, image, body, summary, authors, keywords, publish_date, source_id, created_at, updated_at, url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            article.title,
                            article.top_image,
                            article.article_html,
                            article.summary,
                            ", ".join(article.authors),
                            ", ".join(article.keywords),
                            article.publish_date,
                            id,
                            datetime.now(),
                            datetime.now(),
                            article.url,
                        ),
                    )
                connection.commit()


if __name__ == "__main__":
    with connection.cursor() as cursor:
        cursor.execute("SELECT url, id  FROM sources where active=1")
        source_urls = [elem[0] for elem in cursor.fetchall()]
    crawler = NewsCrawler(source_urls)

    print("Voy a buildear")
    crawler.build_sources()
    print("Voy a crawlear")
    crawler.crawl_articles()
    print("Voy a extraer")
    crawler.extract_information()
