#!/usr/bin/python3
# coding: utf-8
#----------------------------------------------------------
# Récupération de la liste des références de la société DRI
#----------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Analyse de la page
def chercheReferences(page):
    for reference in page.find_all("div", attrs={'class':'ref'}):
        refNom = reference.find('div', attrs={'class':'title'}).string.strip()
        refUrl = reference.find('div', attrs={'class':'link'}).find('a').string.strip()

        print ("- %s (%s)" % (refNom, refUrl))

url = "https://www.dri.fr/references"
try:
    with urlopen(url) as response:
        webPage = BeautifulSoup(response.read(), "html.parser")
        chercheReferences(webPage)
except urllib.error.URLError:
    print ("Impossible d'ouvrir la page %s" % url)
    exit()
