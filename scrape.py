import requests
import pandas as pd

ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

i = 0
for id in top:
    a = requests.get(ROOT + "item/" + str(id) + ".json").json()
    print a

    if 'url' in a:
        articles.append([a['by'], a['descendants'], a['id'], a['score'], a['time'], a['title'], a['type'], a['url']])


df = pd.DataFrame.from_records(articles, columns=['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url'])

df.to_csv("articles.csv", encoding="utf-8", index=False)

