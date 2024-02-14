import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from parse_sites import get_article_data


url = "https://www.clarin.com/politica/gestiones-ultimo-minuto-gobierno-presento-nueva-propuesta-oposicion-dialoguista-tratar-salvar-ley-omnibus_0_U7oHzhhzJ6.html"
article = get_article_data(url)
print(article["publish_date"])
