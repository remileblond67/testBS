import urllib
from bs4 import BeautifulSoup

def chercheArticles():
  for article in page.find_all("article"):
    titre = article.find('h1', attrs={'class':'entry-title'})
    categories = ''
    for catSpan in article.find('span', attrs={'class':'cat-links'}).find_all('a'):
      categories += '\"'+catSpan.string+'"' + " "
    print ("Cat. %s : %s" % (categories, titre.string))

urlNext = "http://remileblond.fr"

while urlNext is not None:
  page = BeautifulSoup(urllib.urlopen(urlNext))
  chercheArticles()
  next = page.find("a", attrs={'class': 'next'})
  if next is not None :
    urlNext = next.get('href')
  else:
    urlNext = None

