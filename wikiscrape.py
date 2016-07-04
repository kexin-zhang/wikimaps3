import re
import urllib.request
import json
import random
import unicodedata
import wikipedia
from urllib.parse import quote

def topic_search(topic):
    topic = topic.strip()
    topic = topic.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + quote(topic)
    response = urllib.request.urlopen(url)
    html = response.read()
    text = html.decode()

    title = re.findall('<title>([^<]+)</title>', text)
    title = title[0]
    i = title.find(' - Wikipedia')
    title = title[:i]

    topics = links(text)
    children = []
    for topic in topics:
        children.append({"name": topic})

#    with open('data.json', 'w') as outfile:
#        json.dump({"name": title, "children": topics}, outfile)
    return {"name": title, "children": children, 'url': url}

def links(text):
    pat = 'href="/wiki/([^"]+)"'
    links = re.findall(pat, text)

    results = []
    for x in random.sample(range(0, len(links)), 10):
        topic = links[x]
        topic = topic.replace('_', ' ')
        if '#' in topic:
            i = topic.find('#')
            topic = topic[:i]
        if 'Category:' in topic:
            i = topic.find(':')
            topic = topic[i+1:]
        if ':' not in topic and topic not in ['Digital object identifier', 'Main Page', 'International Standard Book Number', 'International Standard Serial Number'] and 'ISO' not in topic and 'PubMed' not in topic and 'All articles' not in topic and 'Articles containing' not in topic and 'Articles lacking sources' not in topic and 'Articles needing additional references' not in topic and "Wikipedia articles" not in topic and "Articles with unsourced statements" not in topic:
            results.append(topic)

    return results[0:5]

def summary(topic):
    x = wikipedia.search(topic, results=1)
    return wikipedia.summary(x, sentences=3)
