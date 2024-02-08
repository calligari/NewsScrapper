from newspaper import build


def get_articles(url: str):
    website = build(url, user_agent="Isoroc / 0.0.1")
    articles = [article.url for article in website.articles]
    return articles
