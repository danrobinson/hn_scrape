import requests
from goose import Goose
from lxml import html

"""
To test the scraper with one article
"""

g = Goose()
ROOT = 'https://hacker-news.firebaseio.com/v0/'

"""
The article I'm hard coding in.
"""
ID = 11602536
full_path = 'https://hacker-news.firebaseio.com/v0/item/11602536.json'

top = requests.get(ROOT + 'topstories.json').json()

articles = []

a = requests.get(ROOT + "item/" + str(ID) + ".json").json()

if 'url' in a:
    a_url = a['url']
    g_article = g.extract(url=a_url)
    a_page = requests.get(a_url)
    #a_tree = html.fromstring(a_page.content)
    a_html = a_page.content
    a_title = g_article.title
    a_text = g_article.cleaned_text

    articles.append([a['by'], a['descendants'], a['id'], a['score'], a['time'], a['title'], a['type'], a['url'], [a_html], [a_title], [a_text]])

"""
Write to a file because I don't know how to use the pandas csv export.
"""
with open("article.txt", 'w') as output_html:
        for element in articles:
            for part in element:
                output_html.write("{}\n".format(str(part)))


