import requests
import pandas as pd
from goose import Goose

g = Goose()
ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

i = 0
for id in top:
    if i < 10:

        a = requests.get(ROOT + "item/" + str(id) + ".json").json()
        print a
        i += 1

        if 'url' in a:
            a_url = a['url']
            g_article = g.extract(url=a_url)
            a_page = requests.get(a_url)
            #a_tree = html.fromstring(a_page.content)
            a_html = a_page.content
            a_title = g_article.title
            a_text = g_article.cleaned_text

            articles.append([a['by'], a['descendants'], a['id'], a['score'], a['time'], a['title'], a['type'], a['url'], [a_html], [a_title], [a_text]])
    else:
        pass

df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'html', 'title', 'text'])

df.to_csv("articles.csv", encoding="utf-8", index=False)

i = 0
for article in articles:
    i += 1
    filename = "{0} - {1}.txt".format(i, article[2])
    with open(filename, 'w') as outfile:
        outfile.write(article[10])


