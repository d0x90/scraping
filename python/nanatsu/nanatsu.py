# -*- coding: cp1252 -*-
# The standard library modules
import os
import sys

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
capitulos = [(1038,"Cap�tulo 1 � Los 7 pecados capitales"),(1039,"Cap�tulo 2 � La espada del caballero sagrado"),(1040,"Cap�tulo 3 � Algo que debo hacer"),(1041,"Cap�tulo 4 � El pecado del bosque durmiente"),(1044,"Cap�tulo 5 � Recuerdos en la obscuridad"),(1046,"Cap�tulo 6 � El caballero sagrado Gilthunder"),(1049,"Cap�tulo 7 � El prisionero de la obscuridad"),(1054,"Cap�tulo 8 � El sue�o de una joven chica"),(1057,"Cap�tulo 9 � No puede ser tocado"),(1058,"Cap�tulo 10 � La malicia invisible"),(1059,"Cap�tulo 11 � Incluso si fueras a morir"),(1060,"Cap�tulo 12 � Una batalla confusa"),(1061,"Cap�tulo 13 � Resoluci�n dedicada"),(1062,"Cap�tulo 14"),(1063,"Cap�tulo 15"),(1064,"Cap�tulo 16"),(10705,"Cap�tulo 16.5 � Nada se desperdicia"),(1065,"Cap�tulo 17"),(1066,"Cap�tulo 18"),(1067,"Cap�tulo 19"),(1068,"Cap�tulo 20"),(1069,"Cap�tulo 21"),(1070,"Cap�tulo 22"),(1071,"Cap�tulo 23"),(1072,"Cap�tulo 24"),(1073,"Cap�tulo 25"),(10706,"Cap�tulo 25.5 � Ban el bandido"),(1074,"Cap�tulo 26"),(1075,"Cap�tulo 27"),(1076,"Cap�tulo 28"),(1077,"Cap�tulo 29"),(1078,"Cap�tulo 30"),(1079,"Cap�tulo 31"),(1080,"Cap�tulo 32"),(1081,"Cap�tulo 33"),(1111,"Cap�tulo 34"),(1120,"Cap�tulo 35"),(1131,"Cap�tulo 36"),(1132,"Cap�tulo 37"),(10707,"Cap�tulo 37.5 � La justicia de una chica"),(1133,"Cap�tulo 38"),(1134,"Cap�tulo 39"),(1135,"Cap�tulo 40"),(1136,"Cap�tulo 41"),(10708,"Cap�tulo 41.5 � Extra: la justicia de una chica"),(1137,"Cap�tulo 42"),(1138,"Cap�tulo 43"),(1139,"Cap�tulo 44"),(1140,"Cap�tulo 45"),(1141,"Cap�tulo 46"),(1142,"Cap�tulo 47"),(1143,"Cap�tulo 48"),(1144,"Cap�tulo 49"),(1145,"Cap�tulo 50"),(1146,"Cap�tulo 51"),(1276,"Cap�tulo 52"),(1283,"Cap�tulo 53"),(1453,"Cap�tulo 54"),(1459,"Cap�tulo 55"),(1689,"Cap�tulo 56"),(1690,"Cap�tulo 57"),(1691,"Cap�tulo 58"),(1692,"Cap�tulo 59"),(1693,"Cap�tulo 60"),(1698,"Cap�tulo 61"),(1704,"Cap�tulo 62"),(10709,"Cap�tulo 62.5 � Su lugar"),(1708,"Cap�tulo 63"),(1712,"Cap�tulo 64"),(1717,"Cap�tulo 65"),(1721,"Cap�tulo 66"),(1725,"Cap�tulo 67"),(1729,"Cap�tulo 68"),(1733,"Cap�tulo 69"),(1914,"Cap�tulo 70"),(1915,"Cap�tulo 71"),(1916,"Cap�tulo 72"),(1917,"Cap�tulo 73"),(1955,"Cap�tulo 74"),(1956,"Cap�tulo 75"),(1957,"Cap�tulo 76"),(1958,"Cap�tulo 77"),(1959,"Cap�tulo 78"),(1960,"Cap�tulo 79"),(1961,"Cap�tulo 80"),(1962,"Cap�tulo 81"),(1963,"Cap�tulo 82"),(1964,"Cap�tulo 83"),(1965,"Cap�tulo 84"),(1966,"Cap�tulo 85"),(1967,"Cap�tulo 86"),(1968,"Cap�tulo 87"),(1969,"Cap�tulo 88"),(1970,"Cap�tulo 89"),(1971,"Cap�tulo 90"),(2030,"Cap�tulo 91"),(2031,"Cap�tulo 92"),(2032,"Cap�tulo 93"),(2033,"Cap�tulo 94"),(2034,"Cap�tulo 95"),(2035,"Cap�tulo 96"),(2036,"Cap�tulo 97"),(2037,"Cap�tulo 98"),(2038,"Cap�tulo 99"),(2039,"Cap�tulo 100"),(2040,"Cap�tulo 101"),(2041,"Cap�tulo 102"),(2042,"Cap�tulo 103"),(2043,"Cap�tulo 104"),(2044,"Cap�tulo 105"),(2045,"Cap�tulo 106"),(2046,"Cap�tulo 107"),(2047,"Cap�tulo 108"),(2048,"Cap�tulo 109"),(2049,"Cap�tulo 110"),(2106,"Cap�tulo 111"),(2109,"Cap�tulo 112"),(2112,"Cap�tulo 113"),(2115,"Cap�tulo 114"),(2357,"Cap�tulo 115 � Una vez m�s en la pesadilla"),(2358,"Cap�tulo 116 � Tesoro sagrado LostVayne"),(2359,"Cap�tulo 117 � Los dos reyes hada"),(2360,"Cap�tulo 118 � Choque en el bosque del rey hada"),(2361,"Cap�tulo 119 � Los 10 mandamientos comienzan a moverse"),(2362,"Cap�tulo 120 � Los vampiros de edinburgh parte III"),(2363,"Cap�tulo 121 � Imprevisible"),(2364,"Cap�tulo 122 � El ataque de los demonios"),(2365,"Cap�tulo 123 � Expiaci�n del capit�n de los caballeros santos"),(2366,"Cap�tulo 124 � Lo que la amistad da a luz"),(2367,"Cap�tulo 125 � Derrotar a los 10 mandamientos"),(2368,"Cap�tulo 126 � Donde los recuerdos se dirigen"),(2369,"Cap�tulo 127 � Reuni�n con la desesperaci�n"),(2370,"Cap�tulo 128 � La existencia audaz"),(2371,"Cap�tulo 129 � La tierra sagrada de los druidas"),(2372,"Cap�tulo 130 � El dolor que penetra suavemente"),(2373,"Cap�tulo 131 � La promesa de un ser querido"),(2374,"Cap�tulo 132 � Lo que nos falta"),(2375,"Cap�tulo 133 � Impaciencia y ansiedad"),(2376,"Cap�tulo 134 � A ti, que ya no eres mi capit�n "),(2377,"Cap�tulo 135 � Simples saludos"),(2378,"Cap�tulo 136 � Sembrando el terror"),(2379,"Cap�tulo 137 � Entre t� y yo"),(2380,"Cap�tulo 138 � Batalla con la oscuridad"),(2381,"Cap�tulo 139 � Cu�ntame sobre tu pasado"),(2382,"Cap�tulo 140 � El ladr�n y el ni�o"),(2383,"Cap�tulo 141 � Padre e hijo"),(2384,"Cap�tulo 142 � Donde hay amor"),(2385,"Cap�tulo 143 � Grito de la guardiana sagrada"),(2386,"Cap�tulo 144 � El hombre de la codicia"),(2387,"Cap�tulo 145 � Preciosa alma"),(2388,"Cap�tulo 146 � Coraz�n al desnudo"),(2389,"Cap�tulo 147 � Adi�s, mi amado ladr�n"),(2390,"Cap�tulo 148 � Muerte en la persecuci�n"),(2391,"Cap�tulo 149 � El juego de garan"),(2392,"Cap�tulo 150 � Poder m�gico de garan"),(2393,"Cap�tulo 151 � El maestro del sol"),(2394,"Cap�tulo 152 � Atra�dos por la luz de la vela"),(2395,"Cap�tulo 153 � La confesi�n de Melody"),(2396,"Cap�tulo 154 � El demonio sonr�e"),(2397,"Cap�tulo 155 � El laberinto de trampas mortales"),(2398,"Cap�tulo 156 � Desafi� de exploraci�n del laberinto"),(2399,"Cap�tulo 157 � Ca�tica danza de los desaf�os"),(2400,"Cap�tulo 158 � Los h�roes de revelry"),(2401,"Cap�tulo 159 � No hay necesidad de palabras"),(2402,"Cap�tulo 160 � Vamos! atravesemoslo!"),(2403,"Cap�tulo 161 � El legendario"),(2404,"Cap�tulo 162 � Cu�l ser� el emparejamiento del destino"),(2405,"Cap�tulo 163 � La princesa y la guardiana sagrada"),(2406,"Cap�tulo 164 � Aquellos que nunca se rendir�n"),(2407,"Cap�tulo 165 � La pareja dispareja"),(2408,"Cap�tulo 166 � Fruta extra�a"),(2409,"Cap�tulo 167 � Lo precioso en ti"),(2410,"Cap�tulo 168 � El plan de exterminaci�n a los diez mandamientos"),(2411,"Cap�tulo 169 � El legendario caballero sagrado mas d�bil"),(2412,"Cap�tulo 170 � Para quien brilla esa luz"),(2413,"Cap�tulo 171 � El momento ha llegado"),(2414,"Cap�tulo 172 � A mis antiguos amigos"),(2415,"Cap�tulo 173 � Desciende la oscuridad"),(2416,"Cap�tulo 174 � Meliodas vs los diez mandamientos"),(2417,"Cap�tulo 175 � A mi querido Meliodas"),(2418,"Cap�tulo 176 � Relato de la oscuridad"),(2419,"Cap�tulo 177 � Lo que puedo darte"),(2420,"Cap�tulo 178 � Britannia oscura"),(2421,"Cap�tulo 179 � En busca de esperanza"),(2422,"Cap�tulo 180 � El caballero errante"),(2423,"Cap�tulo 181 � Caballero sagrado Zaratras"),(2424,"Cap�tulo 182 � Calidez incondicional"),(2425,"Cap�tulo 183 � Zona peligrosa"),(2426,"Cap�tulo 184 � Choque de titanes"),(2428,"Cap�tulo 184.5 � Pecados de vacaciones"),(2429,"Cap�tulo 185 � Orgullo vs caridad"),(2430,"Cap�tulo 186 � Batalla por la defensa de liones"),(2431,"Cap�tulo 187 � Los malvados perecer�n"),(2432,"Cap�tulo 188 � La espada y el alma para salvar a los amigos de uno"),(2433,"Cap�tulo 189 � El h�roe se levanta"),(2434,"Cap�tulo 190 � Fest�n del demonio"),(2435,"Cap�tulo 191 � La mujer insaciable"),(2436,"Cap�tulo 192 � La espada y el alma para salvar a un amigo"),(2437,"Cap�tulo 193 � La estrategia del capit�n de los caballeros sagrados"),(2438,"Cap�tulo 194 � Una cruel esperanza"),(2439,"Cap�tulo 195 � La batalla por la defensa de liones concluye"),(2440,"Cap�tulo 196 � Siempre y cuando t� est�s aqu�"),(2441,"Cap�tulo 197 � Respuesta"),(2442,"Cap�tulo 198 � La gigante y el hada"),(2443,"Cap�tulo 199 � Aquellos con luz"),(2444,"Cap�tulo 200 � Memorias de la guerra santa"),(2445,"Cap�tulo 201 � Compa�eros de batalla"),(9367,"Cap�tulo 201.1 � Una manera tierna de disipar la magia"),(9368,"Cap�tulo 201.2 � Lo que quiero decirte"),(9369,"Cap�tulo 201.3 � Reconstruccion del sombrero de jabali"),(9370,"Cap�tulo 201.4 � El compromiso maldito"),(9371,"Cap�tulo 201.5 � Lucha. el gran capitan!"),(11160,"Cap�tulo 201.6 � Lo que quiero decirte "),(11161,"Cap�tulo 201.7 � Reconstrucci�n del boar hat "),(11162,"Cap�tulo 201.8 � El compromiso maldito "),(11163,"Cap�tulo 201.9 � �Lucha, el gran capit�n! "),(4055,"Cap�tulo 202 � El elenco de la guerra santa"),(4056,"Cap�tulo 203 � El plan de Ryudoshel"),(4057,"Cap�tulo 204 � Que haya luz"),(4058,"Cap�tulo 205 � Los 10 mandamientos vs los 4 arc�ngeles"),(4059,"Cap�tulo 206 � La bestia ruge"),(4060,"Cap�tulo 207 � Indura, bestias de la destrucci�n"),(4226,"Cap�tulo 208 � Elizabeth vs Indra"),(4227,"Cap�tulo 209 � Explicame estos sentimientos"),(4280,"Cap�tulo 210 � Turbulencia de emociones"),(9372,"Cap�tulo 211 � Aquellos que dicen Adi�s"),(11164,"Cap�tulo 211.5 � El mu�eco que ansiava amor "),(10520,"Cap�tulo 212 � Un regalo"),(10682,"Cap�tulo 213 � Es esto a lo que llamamos amor"),(10710,"Cap�tulo 214 � No logro llegar a ti desde aqu�l d�a"),(10723,"Cap�tulo 215 � Zeldris el verdugo"),(10724,"Cap�tulo 216 � Adelante, hacia donde est�n los pecados"),(10762,"Cap�tulo 217 � El lugar del coraz�n"),(10778,"Cap�tulo 218 � Nos encontramos de nuevo"),(10789,"Cap�tulo 219 � El descanso de los h�roes"),(11165,"Cap�tulo 220 � El banquete de los heroes "),(11180,"Cap�tulo 221 � Solo s� sincero"),(11197,"Cap�tulo 222 � Los amantes malditos"),(11221,"Cap�tulo 223 � Amantes desconcertados"),(11230,"Cap�tulo 224 � Este es nuestro modo de vida"),(11250,"Cap�tulo 225 � Hacia la ciudad en ruinas"),(11263,"Cap�tulo 226 � Salvaje"),(11276,"Cap�tulo 227 � Choque! choque! choque!"),(11295,"Cap�tulo 228 � La diosa y la doncella sagrada"),(11692,"Cap�tulo 229 � El amor es la fuerza de la doncella"),(11991,"Cap�tulo 230 � Los guerreros elegidos"),(11992,"Cap�tulo 231 � Orgullo vs Ira"),(11993,"Cap�tulo 232 � El todo poderoso vs el m�s grande"),(12014,"Cap�tulo 233 � Da�o"),(12050,"Cap�tulo 234 � Puerta a lo desconocido"),(12055,"Cap�tulo 235 � Una nueva amenaza"),(12152,"Cap�tulo 236 � Encuentro con la desesperaci�n"),(12176,"Cap�tulo 237 � El demonio pacificador"),(12177,"Cap�tulo 238 � Creando una apertura"),(12279,"Cap�tulo 239 � A nuestro capit�n"),(12293,"Cap�tulo 240 � Los cimientos para el futuro"),(12325,"Cap�tulo 241 � Alma hereditaria"),(12326,"Cap�tulo 242 � El final de los 7 pecados capitales"),(12572,"Cap�tulo 243 � Y as�, �l se embarca en su viaje"),(12593,"Cap�tulo 244 � La princesa elegida"),(12615,"Cap�tulo 245 � Marcha de los santos"),(12719,"Cap�tulo 246 � Un encuentro casual"),(12720,"Cap�tulo 247 � Recuperaci�n"),(12981,"Cap�tulo 248 � Nuestra negociaci�n"),(12982,"Cap�tulo 249 � Trato"),(13012,"Cap�tulo 250 � Composicion"),(13025,"Cap�tulo 251 � El pacto de la guerra santa"),(13058,"Cap�tulo 252 � Destino"),(13100,"Cap�tulo 253 � Gracia perdida"),(13268,"Cap�tulo 254 � Camelott En Desesperacion"),(13269,"Cap�tulo 255 � Hijo de la esperanza"),(13344,"Cap�tulo 256 � La perforadora espada sagrada"),(13398,"Cap�tulo 257 � Inicia el contrataque"),(13399,"Cap�tulo 258 � La guerra santa empieza"),(13400,"Cap�tulo 259 � Britannia devastada por la guerra"),(13429,"Cap�tulo 260 � Lo que quiero decirte"),(13438,"Cap�tulo 261 � Un gato perdido"),(14042,"Cap�tulo 262 � Aqu�l retorcido por la obscuridad"),(14109,"Cap�tulo 263 � Estallidos en la oscuridad"),(14189,"Cap�tulo 264 � El Hombre deformado, retorcido y roto"),(14748,"Cap�tulo 265 � Amor devastador"),(15178,"Cap�tulo 266 � El perseguido y el perseguidor"),(15364,"Cap�tulo 267 � Desde los cielos"),(15365,"Cap�tulo 268 � Desde el purgatorio"),(15564,"Cap�tulo 269 � Vida del purgatorio"),(15807,"Cap�tulo 270 � Encuentro con lo desconocido"),(16064,"Cap�tulo 271 � Sentimientos sinceros"),(16107,"Cap�tulo 272 � La eterna batalla"),(16666,"Cap�tulo 273 � Las victimas de la guerra santa"),(17053,"Cap�tulo 274 � El �ngel ca�do de la desesperaci�n, Mael")]
options = Options()
options.add_argument("window-size=1400,600")
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument('user-agent='+user_agent)
capitulos = OrderedDict(capitulos)
#print capitulos
import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

logs = open("nanatsu/logs.txt","a+")
try:
    for num,title in capitulos.items():
        print 'Descargando Capitulo: '+title
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://manga-mx.com/manga/nanatsu-no-taizai/'+str(num)+'/p1')
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "m_img")))
        #waits till the element with the specific id appears
        src = driver.page_source # gets the html source of the page
        #print src
        parser = BeautifulSoup(src,"lxml") # initialize the parser and parse the source "src"

        #list_of_attributes = {"id" : "nums"} # A list of attributes that you want to check in a tag
        #tag = parser.findAll('select',attrs=list_of_attributes) # Get the video tag from the source
        tag = parser.find(id="nums").findAll('option')
        mylist  = set()
        mylist.add(1)
        for t in tag:
            number = re.search("<option.*>(\d+)</option>",str(t)).group(1)
            if number is not None:
                mylist.add(int(number))

        #mylist es la lista de paginas del capitulo

        for page in mylist:
            print 'Descargando Capitulo: '+title+', pagina: '+ str(page)
            driver.get('https://manga-mx.com/manga/nanatsu-no-taizai/'+str(num)+'/p'+str(page))
            try:
                WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.ID, "m_img")))
            except:
                print 'ERROR capitulo: '+title+', pagina: '+ str(page)
            #waits till the element with the specific id appears
            src = driver.page_source # gets the html source of the page
            #print src
            parser = BeautifulSoup(src,"lxml") # initialize the parser and parse the source "src"
            list_of_attributes = {"id" : "m_img"} # A list of attributes that you want to check in a tag
            tag = parser.findAll('img',attrs=list_of_attributes) # Get the video tag from the source

            n = 0 # Specify the index of video element in the web page
            url = tag[n]['src'] # get the src attribute of the video
            if "http" not in url :
                    url = "http:"+url
            r = requests.get(url, stream=True, headers={'User-agent': user_agent})
            if r.status_code == 200:
                directory = "nanatsu/"+title
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print 'Creando carpeta: '+ directory
                try:
                    with open(directory+"/"+str(page)+".jpg", 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                except Exception as exc:
                    print 'Error en el proceso: '+ str(exc)

        logs.write("Capitulo: "+title+", id: "+str(num)+"Descargado completamente")
        driver.quit()
    logs.close()
except Exception as e:
    print 'Error en el proceso: '+ str(e)
    logs.close()
