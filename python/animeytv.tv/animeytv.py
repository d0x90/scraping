# -*- coding: utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import sys
import re
URL = "http://www.animeytv.tv"
#Fichero para guardar la lista de animes
f = open('animes.txt','w')
#Metodo recursivo para guardar los animes
def getAllAnimes(_url):
	html = urlopen(_url)
	bsObj = BeautifulSoup(html,"html.parser")

	items =  bsObj.findAll("div",{"class":"item"})
	for item in items:
		print item.text
		f.write(item.text.encode('utf-8')+"\n")
	
	try:
		siguienteLink = bsObj.find("a",{"class":"navigation next"}).attrs['href']
	except:
		print "Finalizado?..."
		f.close()
		sys.exit(0)
	#Repetir para la siguiente pagina
	getAllAnimes(URL+siguienteLink)

#Método principal
getAllAnimes(URL)
