#You Dont Always Need a Hammer
from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")

#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)

## NOTE : find = findall with limit = 1
# we can search text inside tags too 
#--------------------------
#nameList = bsObj.findAll(text="the prince")
#print(len(nameList))
#--------------------------
#allText = bsObj.findAll(id="text")
#print(allText[0].get_text())
nameList = bsObj.findAll("span",{"class","green"})
for name in nameList:
	print name.get_text()