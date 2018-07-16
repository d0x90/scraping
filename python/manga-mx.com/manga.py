#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The standard library modules
#  TODO: FALTA VERIFICAR EL PROBLEMA CON EL CAPITULO 62.5
import os
import sys
import argparse
# The wget module
import wget
import requests
import shutil

# The BeautifulSoup module
from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import re
import sys
import logging
from collections import OrderedDict

class Mangamx:
    URL_PARAMETER=None
    URL_BASE = None # URL BASE : URL_PARAMETER without the number of the chapter
    BASE_DIR = None # make the manga title as folder name 
    LOGS_BASE_DIR = None
    capitulos = [] #array of chapters
    WINDOW_SIZE = "1400,600" # Config in case u want to see the browser
    options = None #Options for driver
    user_agent = None #User agent random x each chapter

    #FILES
    ERROR_LOG = None
    INFO_LOG  = None
    SUCCESS_DOWNLOADS = None
    SUCCESS_DOWNLOADS_FILENAME = None
    

    
    def __init__(self):
        parser = argparse.ArgumentParser(description='Inserta la url del primer capitulo de tu manga a descargar .')
        parser.add_argument('--url',
                    help='example:https://manga-mx.com/manga/fairy-tail/13631/')
        sargs = parser.parse_args()
        if (sargs.url):
            if not self.validarUrl(sargs.url):
                print "Inserte una URL valida"
            else:
                self.URL_PARAMETER = sargs.url
                
                
                self.SUCCESS_DOWNLOADS_FILENAME = 'downloaded.txt'
                self.openFiles()
                #URL_BASE='https://manga-mx.com/manga/fairy-tail/13631/'
                self.capitulos = self.obtenerListaCapitulos()
                self.main()
        else:
            print "use --help para ayuda"
            
# options for driver: silent mode
    def initOptionsDriver(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=%s" % self.WINDOW_SIZE)         
        ua = UserAgent()
        a = ua.random
        self.user_agent = ua.random
        self.options.add_argument('user-agent=' + self.user_agent)

       
       
    def main(self):
        for num, title in self.capitulos:
            if self.checkIfDownloaded(num):
                continue
            
            self.writeMessage('INFO: Descargando Capitulo: ' + title, 1)
            self.initOptionsDriver()
            driver = webdriver.Chrome(chrome_options=self.options)
            driver.get(self.URL_BASE + str(num) + '/p1')
            print self.URL_BASE+ str(num) + '/p1'
            try:
                success = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "m_img")))
                if success:
                    # waits till the element with the specific id appears
                    src = driver.page_source  # gets the html source of the page
                    #print src
                    parser = BeautifulSoup(src, "lxml")  # initialize the parser and parse the source "src"

                    # list_of_attributes = {"id" : "nums"} # A list of attributes that you want to check in a tag
                    # tag = parser.findAll('select',attrs=list_of_attributes) # Get the video tag from the source
                    tag = parser.find(id="nums").findAll('option')
                    mylist = set()
                    mylist.add(1)
                    for t in tag:
                        number = re.search("<option.*>(\d+)</option>", str(t)).group(1)
                        if number is not None:
                            mylist.add(int(number))

                    # mylist es la lista de paginas del capitulo
                    self.writeMessage("INFO: paginas: " + str(mylist), 1)
                    for page in mylist:
                        self.writeMessage('INFO: Descargando Capitulo: ' + title + ', pagina: ' + str(page), 1)
                        driver.get(self.URL_BASE + str(num) + '/p' + str(page))
                        try:
                            WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.ID, "m_img")))
                            # waits till the element with the specific id appears
                            src = driver.page_source  # gets the html source of the page
                            # print src
                            parser = BeautifulSoup(src, "lxml")  # initialize the parser and parse the source "src"
                            list_of_attributes = {"id": "m_img"}  # A list of attributes that you want to check in a tag
                            tag = parser.findAll('img', attrs=list_of_attributes)  # Get the video tag from the source

                            n = 0  # Specify the index of video element in the web page
                            url = tag[n]['src']  # get the src attribute of the video
                            if "http" not in url:
                                url = "http:" + url
                            try:
                                r = requests.get(url, stream=True,
                                                 headers={'User-agent': self.user_agent, 'Connection': 'keep-alive'})
                                if r.status_code == 200:
                                    directory = os.path.join(self.BASE_DIR,title)
                                    print directory
                                    if not os.path.exists(directory):
                                        os.makedirs(directory)
                                        self.writeMessage('INFO: Carpeta creada: ' + directory, 1)
                                    groups = re.search('.*?\/\d+\/.*\.([a-zA-Z]{3,3})\?\d+', url)
                                    if groups:
                                        fname = str(page) + "." + str(groups.group(1))
                                    else:
                                        fname = str(page) + ".jpg"
                                    with open(os.path.join(directory, fname), 'wb') as f:
                                        r.raw.decode_content = True
                                        shutil.copyfileobj(r.raw, f)
                            except Exception as exc:
                                self.writeMessage('ERROR: URL con problemas: ' + str(url), 2)
                                self.writeMessage(
                                    'ERROR: Error en la descarga del capitulo: ' + title + ', en la pagina: ' + str(
                                        page) + "\n desc: " + str(exc), 2)
                                pass
                        except Exception as exx:
                            self.writeMessage('ERROR: capitulo: ' + title + ', pagina: ' + str(page), 2)
                            self.writeMessage(str(exx), 2)
                            pass

                    self.writeMessage("INFO: Capitulo: " + title + ", id: " + str(num) + "Descargado completamente", 1)
                    self.SUCCESS_DOWNLOADS.write(str(num) + "\n")
                    driver.quit()
            except:
                pass

        self.INFO_LOG.close()
        self.ERROR_LOG.close()
        self.SUCCESS_DOWNLOADS.close()


#Valida la url recibida como parametro, y tambien define las variables URL_BASE, BASE_DIR
#y crea un directorio con el nombre del manga a descargar para poner todo el contenido ahi 

    def validarUrl(self,url):
        pattern = "(http:|https:)[\/]{2,2}manga-mx.com/manga/([1-9a-zA-Z-]+)/(\d+)/?"
        groups = re.search(pattern,url)
        if groups:
            print "Manga a descargar: " + groups.group(2)
            self.URL_BASE = 'https://manga-mx.com/manga/'+groups.group(2)+"/"
            self.BASE_DIR = groups.group(2)
            self.createDirIfNotExists(self.BASE_DIR)
            return True
        return False

###Abre los ficheros a utilizar para logs y para guardar los capitulos
    def openFiles(self):
        self.LOGS_BASE_DIR     = os.path.join(self.BASE_DIR,"logs")
        self.createDirIfNotExists(self.LOGS_BASE_DIR)
        self.INFO_LOG          = open(os.path.join(self.LOGS_BASE_DIR,"info.logs"), "a+")
        self.ERROR_LOG         = open(os.path.join(self.LOGS_BASE_DIR,"error.logs"), "a+")
        self.SUCCESS_DOWNLOADS = open(os.path.join(self.BASE_DIR,"downloaded.txt"), "a+")


###Crea el directorio recibido x parametro
    def createDirIfNotExists(self,dirName):
        try:
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                if self.INFO_LOG != None:
                    self.writeMessage('INFO: Creando carpeta: ' + dirName, 1)
                
        except Exception as e:
            if self.ERROR_LOG != None:
                self.writeMessage('ERROR AL CREAR LA CARPETA: ' + dirName,2)
    


###Imprime en pantalla y escribe en el archivo logs

    def writeMessage(self,msg, level):
        print msg + "\n"
        try:
            if level == 1:
                self.INFO_LOG.write(msg + "\n")
            else:
                self.ERROR_LOG.write(msg + "\n")
        except Exception as e:
            print str(e)


###Revisa el archivo *.downloads.txt
###Y verifica si el capitulo a descargar esta en esa lista, si esta descargado, intenta con el siguiente.

    def checkIfDownloaded(self,num):
        try:
            with open(os.path.join(self.BASE_DIR,self.SUCCESS_DOWNLOADS_FILENAME), 'r') as descargados:
                for cap in descargados:
                    if int(num) == int(cap):
                        self.writeMessage("INFO: Capitulo ya descargado: " + str(num), 1)
                        return True                     
        except Exception as e:
            self.writeMessage('Error verificando las descargas: '+str(e),2)
            pass


###Obtiene la lista inicial de los capitulos a descargar
###devuelve el array ordenado
    def obtenerListaCapitulos(self):
        self.initOptionsDriver()
        driver = webdriver.Chrome(chrome_options=self.options)
        driver.get(self.URL_PARAMETER)
        try:
            success = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "c_list")))
            if success:
                src = driver.page_source
                parser = BeautifulSoup(src, "lxml")  # initialize the parser and parse the source "src"
                tag = parser.find(id="c_list").findAll('option')
                for t in tag:
                    #print t
                    item = re.search("<option.*?//.*/(\d+).*>(.*)</option>",str(t))
                    if item:
                        numero = item.group(1)
                        capitulo = item.group(2)
                        self.capitulos.append((numero,capitulo))
        except Exception as e:
            print str(e)
        driver.quit()
        #print self.capitulos
        return list(reversed(self.capitulos))
        


mangamx = Mangamx()
