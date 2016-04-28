import requests

ROOT = 'https://hacker-news.firebaseio.com/v0/'

top = requests.get(ROOT + 'topstories.json').json()

articles = [['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url']]

i = 0
for id in top:
    a = requests.get(ROOT + "item/" + str(id) + ".json").json()
    print a

    if 'url' in a:
        articles.append([a['by'], a['descendants'], a['id'], a['score'], a['time'], a['title'], a['type'], a['url']])







