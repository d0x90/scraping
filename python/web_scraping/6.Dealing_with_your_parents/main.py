from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")
#1. get <img>
#2. get <td> of <img>
#3. get the previous <td>
#4. get text =  $ 15.00
print bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()