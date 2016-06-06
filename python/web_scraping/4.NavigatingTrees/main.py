#
from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

#If you want to find only descendants that are children, you can use the .children tag
#It’s definitely important to differentiate between children and descendants!
for child in bsObj.find("table",{"id":"giftList"}).children:
	print child