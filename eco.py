import requests
from bs4 import BeautifulSoup
import re
import random


def get_articles():
    """
    write a text file with article links from the minimalists blog
    """
    link = requests.get('https://www.theminimalists.com/archives/')
    key_text_url = "https://www.theminimalists.com/"
    f = open("links_minimalists.txt", "a")
    soup = BeautifulSoup(link.text, 'html.parser')
    for art in soup.find_all('a', href=True):
        if re.search(key_text_url, art.get('href')):
            f.write(f"{art['href']}\n")
    f.close()


def get_recomendation():
    """
    Read links saved about minimalist blogs and choose an aleatory number
    to suggest that article to the user
    """
    list_links = []
    f = open("links_minimalists.txt", "r")
    for i in f:
        list_links.append(i)
    return  list_links


def choose_article(articles: list) -> str:
    n = random.randint(0, len(articles) - 1)
    return articles[n]


tips_lists = get_recomendation()
print(choose_article(tips_lists))
