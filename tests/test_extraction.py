import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from parse_sites import get_article_data


url = "https://www.clarin.com/politica/gestiones-ultimo-minuto-gobierno-presento-nueva-propuesta-oposicion-dialoguista-tratar-salvar-ley-omnibus_0_U7oHzhhzJ6.html"
article = get_article_data(url)
assert (
    article["title"]
    == "Gestiones de último minuto: el Gobierno negoció con la oposición dialoguista para tratar de salvar la Ley Ómnibus"
)
assert (
    article["top_image"]
    == "https://www.clarin.com/img/2024/02/06/jStZLEWhl_2000x1500__1.jpg"
)
print("Test passed!")
