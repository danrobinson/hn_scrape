import requests
import pandas as pd
from goose import Goose

g = Goose()
ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

i = 0
for id in top:
    a = requests.get(ROOT + "item/" + str(id) + ".json").json()
    print a

    if 'url' in a:
        a_url = a['url']
        g_article = g.extract(url=a_url)
        a_page = requests.get(a_url)
        #a_tree = html.fromstring(a_page.content)
        a_html = a_page.content
        a_title = g_article.title
        a_text = g_article.cleaned_text

        articles.append([a['by'], a['descendants'], a['id'], a['score'], a['time'], a['title'], a['type'], a['url'], [a_html], [a_title], [a_text]])


df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html', 'title', 'text'])

df.to_csv("articles.csv", encoding="utf-8", index=False)

