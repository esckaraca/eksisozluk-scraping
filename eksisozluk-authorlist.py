import requests
from bs4 import BeautifulSoup

def start(url):
    pagenumlist = []
    hreflist = []
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')

    for link in soup.find_all('ul', {'class': 'topic-list'}):
        for topic in link.find_all('a'):
            href = 'https://eksisozluk.com' + topic.get('href')
            hreflist.append(href)
            # print(href)

    for pagenumber in soup.find_all('small'):
        pagenumlist.append(pagenumber.string)
        # print(pagenumber.string)

    zippo = zip(hreflist, pagenumlist)

    for a, b in zippo:
        max_page = 1
        print(a + " " + b)
        while max_page <= int(b):
            topic_url = a + '&p=' + str(max_page)
            source_code = requests.get(topic_url)
            soup_author = BeautifulSoup(source_code.text, 'html.parser')
            for author_list in soup_author.find_all('a', {'class': 'entry-author'}):
                print(author_list.string)
            max_page += 1
        continue

start('http://www.eksisozluk.com')
