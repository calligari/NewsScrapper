from newspaper import build, Article
import nltk

nltk.download("punkt")


def get_articles(url: str):
    try:
        website = build(url, user_agent="Isoroc / 0.0.1", number_threads=12)
        articles = [article.url for article in website.articles]
        return articles
    except Exception as e:
        print("Error parsing website:", e)
        return []


def get_article_data(url: str):
    article = Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()

        return {
            "title": article.title,
            "top_image": article.top_image,
            "publish_date": article.publish_date,
            "body": article.text,
            "authors": ", ".join(str(element) for element in article.authors),
            "keywords": ", ".join(str(element) for element in article.keywords),
            "summary": article.summary,
            "url": url,
        }
    except Exception as e:
        print("Error parsing article:", e)
        return {}
