from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

# Esto obtiene todos los TR exceptuando la de los nombres de columnas
#next_sibling solo obtiene los hermanos, como uno no puede ser hermano consigo mismo
#no se toma en cuenta ( en este caso la fila de los nombres de columnas)
# bsObj.find("table",{"id":"giftList"}).tr  = fila de los nombres de columnas
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
	print sibling