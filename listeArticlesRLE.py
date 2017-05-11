#!/usr/bin/python
import urllib.request
from bs4 import BeautifulSoup

# Analyse du contenu de la page
def chercheArticles(page):
  for article in page.find_all("article"):
    titre = article.find('h1', attrs={'class':'entry-title'})
    categories = ''
    for catSpan in article.find('span', attrs={'class':'cat-links'}).find_all('a'):
      categories += '\"'+catSpan.string+'"' + " "
    print ("Cat. %s : %s" % (categories, titre.string))

urlNext = "http://remileblond.fr"

# Parcours des pages du site
while urlNext is not None:
  try:
      with urllib.request.urlopen(urlNext) as response:
        webResponse = response.read()
        webPage = BeautifulSoup(webResponse, "html.parser")
        chercheArticles(webPage)
        next = webPage.find("a", attrs={'class': 'next'})
        if next is not None :
            urlNext = next.get('href')
        else:
            urlNext = None
  except urllib.error.URLError:
      print ("Impossible d'ouvrir la page %s" % urlNext)
      exit()
