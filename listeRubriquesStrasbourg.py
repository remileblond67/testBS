#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup

# Analyse du contenu de la page
def chercheArticles(page):
  with page.find('div', attrs={'id':'theme-menu'}) as menu:
      print (menu)

urlNext = "http://strasbourg.eu"
try:
  with urllib.request.urlopen(urlNext) as response:
    webResponse = response.read()
    with BeautifulSoup(webResponse, "html.parser") as webPage:
        chercheArticles(webPage)

except urllib.error.URLError:
  print ("Impossible d'ouvrir la page %s" % urlNext)
  exit()
