import base64
import urllib
import time
import cv2
import numpy as np
from StringIO import StringIO
from bs4 import BeautifulSoup
from mechanize import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium import webdriver
from PIL import Image
import pytesseract



chromedriver = "C:/Users/Diego Campos/chromedriver_win32/chromedriver.exe"
url = "https://apps.contraloria.gob.pe/ciudadano/wfm_obras_buscador.aspx"
driver = webdriver.Chrome(chromedriver)
driver.get(url)

def rellenarCampos():
    #Seleccionar Departamento
    departamento = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlDepartamento"]""")))
    driver.find_element_by_xpath("""//*[@id="ddlDepartamento"]/option[15]""").click()
    #Seleccionar Provincia
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlProvincia"]""")))
    driver.find_element_by_xpath("""//*[@id="ddlProvincia"]/option[2]""").click()
    #Seleccionar Distrito
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"""//*[@id="ddlDistrito"]""")))
    driver.find_element_by_xpath("""//*[@id="ddlDistrito"]/option[2]""").click()
    #Resolver Captcha
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"imgCaptcha")))

def capturarCaptcha():
    image_element = driver.find_element_by_xpath("""//*[@id="form1"]/div[2]/div[8]""")
    action_chain = ActionChains(driver)
    action_chain.move_to_element(image_element)
    action_chain.perform()

    loc, size = image_element.location_once_scrolled_into_view, image_element.size
    left, top = loc['x'], loc['y']

    width, height = size['width'], size['height']
    box = (int(left), int(top), int(left + width), int(top + height))

    screenshot = driver.save_screenshot("captcha.png")
    img = Image.open('captcha.png')
    captcha = img.crop(box)
    captcha.save('captcha.png', 'PNG')

def procesarCaptcha():

    #MEJORANDO LA IMAGEN ANTES DE USAR OCR?
    img = cv2.imread("captcha.png")
    boundaries = [
            ([0, 100, 0], [255, 255, 255])
    ]
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        output = cv2.inRange(img, lower, upper)    
        cv2.imwrite("captcha2.png", output)
    
def extraerTexto():
    #aplicando OCR a la imagen
    image = Image.open('captcha2.png')
    image.load()
    #r, g, b, a = image.split()		#removing the alpha channel
    #image = Image.merge('RGB',(r,g,b))    
    resuelto = pytesseract.image_to_string(image).strip().replace(" ","")
    print "Captcha: " + resuelto
    return resuelto
    #submit

def enviarForm():
    driver.find_element_by_xpath("""//*[@id="txtCodCaptcha"]""").send_keys(extraerTexto())
    time.sleep(5)
    driver.find_element_by_xpath("""//*[@id="Buscar"]""").click()


rellenarCampos()
capturarCaptcha()
procesarCaptcha()
enviarForm()



