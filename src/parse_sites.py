from newspaper import build, Article
import nltk

nltk.download("punkt")


def get_articles(url: str):
    website = build(url, user_agent="Isoroc / 0.0.1")
    articles = [article.url for article in website.articles]
    return articles


def get_article_data(url: str):
    article = Article(url)
    article.download()
    article.parse()
    # article.nlp()
    #
    return {
        "title": article.title,
        "top_image": article.top_image,
        "publish_date": article.publish_date,
        "body": article.text,
        # "keywords": article.keywords,
        # "summary": article.summary,
        "url": url,
    }
