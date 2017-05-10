#!/usr/bin/python
import urllib
from bs4 import BeautifulSoup

def chercheArticles():
  for article in page.find_all("article", attrs={'class':'postItem'}):
    titre = article.find(attrs={'class':'title'})
    try:
      print ("%s" % titre.string)
    except AttributeError:
      print (article)
      exit()

urlNext = "http://weelz.fr"

while urlNext is not None:
  page = BeautifulSoup(urllib.urlopen(urlNext))
  chercheArticles()
  next = page.find("li", attrs={'class': 'nav next'})
  try:
    urlNext = next.find('a').get('href')
  except AttributeError:
    exit()

