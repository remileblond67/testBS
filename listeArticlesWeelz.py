#!/usr/bin/python3
# coding: utf-8
import urllib.request
from bs4 import BeautifulSoup

# Recherche les articles dans la page
def chercheArticles(page):
  for article in page.find_all("article", attrs={'class':'postItem'}):
    titre = article.find(attrs={'class':'title'})
    try:
      print ("%s" % titre.string)
    except AttributeError:
      print (article)
      exit()

urlNext = "http://weelz.fr"

# Parcours des pages du site
while urlNext is not None:
  try:
      with urllib.request.urlopen(urlNext) as response:
        webResponse = response.read()
        webPage = BeautifulSoup(webResponse, "html.parser")
        chercheArticles(webPage)
        next = webPage.find("li", attrs={'class': 'nav next'})
        if next is not None :
            urlNext = next.find('a').get('href')
        else:
            urlNext = None
  except urllib.error.URLError:
      print ("Impossible d'ouvrir la page %s" % urlNext)
      exit()
