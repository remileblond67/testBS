#!/usr/bin/python3
# coding: utf-8
#----------------------------------------------------------
# Récupération de la liste des clubs photos de l'UR21
#----------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Analyse de la page
def chercheClub(page):
    for tableau in page.find_all("table", attrs={'class':'spip'}):
        for tbody in tableau.find_all("tbody"):
            for ligne in tbody.find_all("tr"):
                nbCol = 1
                for col in ligne.find_all("td"):
                    if (nbCol == 2) :
                        nomClub = col.string
                    if (nbCol == 4) :
                        villeClub = col.string
                    if (nbCol == 5) :
                        try:
                            emailClub = col.find("a").get('title').replace('..åt..', '@')
                        except:
                            emailClub = ""
                        
                    if (nbCol == 6) :
                        try:
                            lienClub = col.find("a").get('href')
                        except:
                            lienClub = ""
                        print ("<li><b>%s</b> à %s. Adresse de contact : %s <a href='%s'>%s</a></li>"%(nomClub, villeClub, emailClub, lienClub, lienClub))
                        # print (emailClub)
                    
                    nbCol = nbCol+1

url = "http://ur21.federation-photo.fr/photo-clubs/"
try:
    with urlopen(url) as response:
        webPage = BeautifulSoup(response.read(), "html.parser")
        chercheClub(webPage)
except urllib.error.URLError:
    print ("Impossible d'ouvrir la page %s" % url)
    exit()
