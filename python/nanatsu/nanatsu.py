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
capitulos = [(1038,"Capítulo 1 — Los 7 pecados capitales"),(1039,"Capítulo 2 — La espada del caballero sagrado"),(1040,"Capítulo 3 — Algo que debo hacer"),(1041,"Capítulo 4 — El pecado del bosque durmiente"),(1044,"Capítulo 5 — Recuerdos en la obscuridad"),(1046,"Capítulo 6 — El caballero sagrado Gilthunder"),(1049,"Capítulo 7 — El prisionero de la obscuridad"),(1054,"Capítulo 8 — El sueño de una joven chica"),(1057,"Capítulo 9 — No puede ser tocado"),(1058,"Capítulo 10 — La malicia invisible"),(1059,"Capítulo 11 — Incluso si fueras a morir"),(1060,"Capítulo 12 — Una batalla confusa"),(1061,"Capítulo 13 — Resolución dedicada"),(1062,"Capítulo 14"),(1063,"Capítulo 15"),(1064,"Capítulo 16"),(10705,"Capítulo 16.5 — Nada se desperdicia"),(1065,"Capítulo 17"),(1066,"Capítulo 18"),(1067,"Capítulo 19"),(1068,"Capítulo 20"),(1069,"Capítulo 21"),(1070,"Capítulo 22"),(1071,"Capítulo 23"),(1072,"Capítulo 24"),(1073,"Capítulo 25"),(10706,"Capítulo 25.5 — Ban el bandido"),(1074,"Capítulo 26"),(1075,"Capítulo 27"),(1076,"Capítulo 28"),(1077,"Capítulo 29"),(1078,"Capítulo 30"),(1079,"Capítulo 31"),(1080,"Capítulo 32"),(1081,"Capítulo 33"),(1111,"Capítulo 34"),(1120,"Capítulo 35"),(1131,"Capítulo 36"),(1132,"Capítulo 37"),(10707,"Capítulo 37.5 — La justicia de una chica"),(1133,"Capítulo 38"),(1134,"Capítulo 39"),(1135,"Capítulo 40"),(1136,"Capítulo 41"),(10708,"Capítulo 41.5 — Extra: la justicia de una chica"),(1137,"Capítulo 42"),(1138,"Capítulo 43"),(1139,"Capítulo 44"),(1140,"Capítulo 45"),(1141,"Capítulo 46"),(1142,"Capítulo 47"),(1143,"Capítulo 48"),(1144,"Capítulo 49"),(1145,"Capítulo 50"),(1146,"Capítulo 51"),(1276,"Capítulo 52"),(1283,"Capítulo 53"),(1453,"Capítulo 54"),(1459,"Capítulo 55"),(1689,"Capítulo 56"),(1690,"Capítulo 57"),(1691,"Capítulo 58"),(1692,"Capítulo 59"),(1693,"Capítulo 60"),(1698,"Capítulo 61"),(1704,"Capítulo 62"),(10709,"Capítulo 62.5 — Su lugar"),(1708,"Capítulo 63"),(1712,"Capítulo 64"),(1717,"Capítulo 65"),(1721,"Capítulo 66"),(1725,"Capítulo 67"),(1729,"Capítulo 68"),(1733,"Capítulo 69"),(1914,"Capítulo 70"),(1915,"Capítulo 71"),(1916,"Capítulo 72"),(1917,"Capítulo 73"),(1955,"Capítulo 74"),(1956,"Capítulo 75"),(1957,"Capítulo 76"),(1958,"Capítulo 77"),(1959,"Capítulo 78"),(1960,"Capítulo 79"),(1961,"Capítulo 80"),(1962,"Capítulo 81"),(1963,"Capítulo 82"),(1964,"Capítulo 83"),(1965,"Capítulo 84"),(1966,"Capítulo 85"),(1967,"Capítulo 86"),(1968,"Capítulo 87"),(1969,"Capítulo 88"),(1970,"Capítulo 89"),(1971,"Capítulo 90"),(2030,"Capítulo 91"),(2031,"Capítulo 92"),(2032,"Capítulo 93"),(2033,"Capítulo 94"),(2034,"Capítulo 95"),(2035,"Capítulo 96"),(2036,"Capítulo 97"),(2037,"Capítulo 98"),(2038,"Capítulo 99"),(2039,"Capítulo 100"),(2040,"Capítulo 101"),(2041,"Capítulo 102"),(2042,"Capítulo 103"),(2043,"Capítulo 104"),(2044,"Capítulo 105"),(2045,"Capítulo 106"),(2046,"Capítulo 107"),(2047,"Capítulo 108"),(2048,"Capítulo 109"),(2049,"Capítulo 110"),(2106,"Capítulo 111"),(2109,"Capítulo 112"),(2112,"Capítulo 113"),(2115,"Capítulo 114"),(2357,"Capítulo 115 — Una vez más en la pesadilla"),(2358,"Capítulo 116 — Tesoro sagrado LostVayne"),(2359,"Capítulo 117 — Los dos reyes hada"),(2360,"Capítulo 118 — Choque en el bosque del rey hada"),(2361,"Capítulo 119 — Los 10 mandamientos comienzan a moverse"),(2362,"Capítulo 120 — Los vampiros de edinburgh parte III"),(2363,"Capítulo 121 — Imprevisible"),(2364,"Capítulo 122 — El ataque de los demonios"),(2365,"Capítulo 123 — Expiación del capitán de los caballeros santos"),(2366,"Capítulo 124 — Lo que la amistad da a luz"),(2367,"Capítulo 125 — Derrotar a los 10 mandamientos"),(2368,"Capítulo 126 — Donde los recuerdos se dirigen"),(2369,"Capítulo 127 — Reunión con la desesperación"),(2370,"Capítulo 128 — La existencia audaz"),(2371,"Capítulo 129 — La tierra sagrada de los druidas"),(2372,"Capítulo 130 — El dolor que penetra suavemente"),(2373,"Capítulo 131 — La promesa de un ser querido"),(2374,"Capítulo 132 — Lo que nos falta"),(2375,"Capítulo 133 — Impaciencia y ansiedad"),(2376,"Capítulo 134 — A ti, que ya no eres mi capitán "),(2377,"Capítulo 135 — Simples saludos"),(2378,"Capítulo 136 — Sembrando el terror"),(2379,"Capítulo 137 — Entre tú y yo"),(2380,"Capítulo 138 — Batalla con la oscuridad"),(2381,"Capítulo 139 — Cuéntame sobre tu pasado"),(2382,"Capítulo 140 — El ladrón y el niño"),(2383,"Capítulo 141 — Padre e hijo"),(2384,"Capítulo 142 — Donde hay amor"),(2385,"Capítulo 143 — Grito de la guardiana sagrada"),(2386,"Capítulo 144 — El hombre de la codicia"),(2387,"Capítulo 145 — Preciosa alma"),(2388,"Capítulo 146 — Corazón al desnudo"),(2389,"Capítulo 147 — Adiós, mi amado ladrón"),(2390,"Capítulo 148 — Muerte en la persecución"),(2391,"Capítulo 149 — El juego de garan"),(2392,"Capítulo 150 — Poder mágico de garan"),(2393,"Capítulo 151 — El maestro del sol"),(2394,"Capítulo 152 — Atraídos por la luz de la vela"),(2395,"Capítulo 153 — La confesión de Melody"),(2396,"Capítulo 154 — El demonio sonríe"),(2397,"Capítulo 155 — El laberinto de trampas mortales"),(2398,"Capítulo 156 — Desafió de exploración del laberinto"),(2399,"Capítulo 157 — Caótica danza de los desafíos"),(2400,"Capítulo 158 — Los héroes de revelry"),(2401,"Capítulo 159 — No hay necesidad de palabras"),(2402,"Capítulo 160 — Vamos! atravesemoslo!"),(2403,"Capítulo 161 — El legendario"),(2404,"Capítulo 162 — Cuál será el emparejamiento del destino"),(2405,"Capítulo 163 — La princesa y la guardiana sagrada"),(2406,"Capítulo 164 — Aquellos que nunca se rendirán"),(2407,"Capítulo 165 — La pareja dispareja"),(2408,"Capítulo 166 — Fruta extraña"),(2409,"Capítulo 167 — Lo precioso en ti"),(2410,"Capítulo 168 — El plan de exterminación a los diez mandamientos"),(2411,"Capítulo 169 — El legendario caballero sagrado mas débil"),(2412,"Capítulo 170 — Para quien brilla esa luz"),(2413,"Capítulo 171 — El momento ha llegado"),(2414,"Capítulo 172 — A mis antiguos amigos"),(2415,"Capítulo 173 — Desciende la oscuridad"),(2416,"Capítulo 174 — Meliodas vs los diez mandamientos"),(2417,"Capítulo 175 — A mi querido Meliodas"),(2418,"Capítulo 176 — Relato de la oscuridad"),(2419,"Capítulo 177 — Lo que puedo darte"),(2420,"Capítulo 178 — Britannia oscura"),(2421,"Capítulo 179 — En busca de esperanza"),(2422,"Capítulo 180 — El caballero errante"),(2423,"Capítulo 181 — Caballero sagrado Zaratras"),(2424,"Capítulo 182 — Calidez incondicional"),(2425,"Capítulo 183 — Zona peligrosa"),(2426,"Capítulo 184 — Choque de titanes"),(2428,"Capítulo 184.5 — Pecados de vacaciones"),(2429,"Capítulo 185 — Orgullo vs caridad"),(2430,"Capítulo 186 — Batalla por la defensa de liones"),(2431,"Capítulo 187 — Los malvados perecerán"),(2432,"Capítulo 188 — La espada y el alma para salvar a los amigos de uno"),(2433,"Capítulo 189 — El héroe se levanta"),(2434,"Capítulo 190 — Festín del demonio"),(2435,"Capítulo 191 — La mujer insaciable"),(2436,"Capítulo 192 — La espada y el alma para salvar a un amigo"),(2437,"Capítulo 193 — La estrategia del capitán de los caballeros sagrados"),(2438,"Capítulo 194 — Una cruel esperanza"),(2439,"Capítulo 195 — La batalla por la defensa de liones concluye"),(2440,"Capítulo 196 — Siempre y cuando tú estés aquí"),(2441,"Capítulo 197 — Respuesta"),(2442,"Capítulo 198 — La gigante y el hada"),(2443,"Capítulo 199 — Aquellos con luz"),(2444,"Capítulo 200 — Memorias de la guerra santa"),(2445,"Capítulo 201 — Compañeros de batalla"),(9367,"Capítulo 201.1 — Una manera tierna de disipar la magia"),(9368,"Capítulo 201.2 — Lo que quiero decirte"),(9369,"Capítulo 201.3 — Reconstruccion del sombrero de jabali"),(9370,"Capítulo 201.4 — El compromiso maldito"),(9371,"Capítulo 201.5 — Lucha. el gran capitan!"),(11160,"Capítulo 201.6 — Lo que quiero decirte "),(11161,"Capítulo 201.7 — Reconstrucción del boar hat "),(11162,"Capítulo 201.8 — El compromiso maldito "),(11163,"Capítulo 201.9 — ¡Lucha, el gran capitán! "),(4055,"Capítulo 202 — El elenco de la guerra santa"),(4056,"Capítulo 203 — El plan de Ryudoshel"),(4057,"Capítulo 204 — Que haya luz"),(4058,"Capítulo 205 — Los 10 mandamientos vs los 4 arcángeles"),(4059,"Capítulo 206 — La bestia ruge"),(4060,"Capítulo 207 — Indura, bestias de la destrucción"),(4226,"Capítulo 208 — Elizabeth vs Indra"),(4227,"Capítulo 209 — Explicame estos sentimientos"),(4280,"Capítulo 210 — Turbulencia de emociones"),(9372,"Capítulo 211 — Aquellos que dicen Adiós"),(11164,"Capítulo 211.5 — El muñeco que ansiava amor "),(10520,"Capítulo 212 — Un regalo"),(10682,"Capítulo 213 — Es esto a lo que llamamos amor"),(10710,"Capítulo 214 — No logro llegar a ti desde aquél día"),(10723,"Capítulo 215 — Zeldris el verdugo"),(10724,"Capítulo 216 — Adelante, hacia donde están los pecados"),(10762,"Capítulo 217 — El lugar del corazón"),(10778,"Capítulo 218 — Nos encontramos de nuevo"),(10789,"Capítulo 219 — El descanso de los héroes"),(11165,"Capítulo 220 — El banquete de los heroes "),(11180,"Capítulo 221 — Solo sé sincero"),(11197,"Capítulo 222 — Los amantes malditos"),(11221,"Capítulo 223 — Amantes desconcertados"),(11230,"Capítulo 224 — Este es nuestro modo de vida"),(11250,"Capítulo 225 — Hacia la ciudad en ruinas"),(11263,"Capítulo 226 — Salvaje"),(11276,"Capítulo 227 — Choque! choque! choque!"),(11295,"Capítulo 228 — La diosa y la doncella sagrada"),(11692,"Capítulo 229 — El amor es la fuerza de la doncella"),(11991,"Capítulo 230 — Los guerreros elegidos"),(11992,"Capítulo 231 — Orgullo vs Ira"),(11993,"Capítulo 232 — El todo poderoso vs el más grande"),(12014,"Capítulo 233 — Daño"),(12050,"Capítulo 234 — Puerta a lo desconocido"),(12055,"Capítulo 235 — Una nueva amenaza"),(12152,"Capítulo 236 — Encuentro con la desesperación"),(12176,"Capítulo 237 — El demonio pacificador"),(12177,"Capítulo 238 — Creando una apertura"),(12279,"Capítulo 239 — A nuestro capitán"),(12293,"Capítulo 240 — Los cimientos para el futuro"),(12325,"Capítulo 241 — Alma hereditaria"),(12326,"Capítulo 242 — El final de los 7 pecados capitales"),(12572,"Capítulo 243 — Y así, él se embarca en su viaje"),(12593,"Capítulo 244 — La princesa elegida"),(12615,"Capítulo 245 — Marcha de los santos"),(12719,"Capítulo 246 — Un encuentro casual"),(12720,"Capítulo 247 — Recuperación"),(12981,"Capítulo 248 — Nuestra negociación"),(12982,"Capítulo 249 — Trato"),(13012,"Capítulo 250 — Composicion"),(13025,"Capítulo 251 — El pacto de la guerra santa"),(13058,"Capítulo 252 — Destino"),(13100,"Capítulo 253 — Gracia perdida"),(13268,"Capítulo 254 — Camelott En Desesperacion"),(13269,"Capítulo 255 — Hijo de la esperanza"),(13344,"Capítulo 256 — La perforadora espada sagrada"),(13398,"Capítulo 257 — Inicia el contrataque"),(13399,"Capítulo 258 — La guerra santa empieza"),(13400,"Capítulo 259 — Britannia devastada por la guerra"),(13429,"Capítulo 260 — Lo que quiero decirte"),(13438,"Capítulo 261 — Un gato perdido"),(14042,"Capítulo 262 — Aquél retorcido por la obscuridad"),(14109,"Capítulo 263 — Estallidos en la oscuridad"),(14189,"Capítulo 264 — El Hombre deformado, retorcido y roto"),(14748,"Capítulo 265 — Amor devastador"),(15178,"Capítulo 266 — El perseguido y el perseguidor"),(15364,"Capítulo 267 — Desde los cielos"),(15365,"Capítulo 268 — Desde el purgatorio"),(15564,"Capítulo 269 — Vida del purgatorio"),(15807,"Capítulo 270 — Encuentro con lo desconocido"),(16064,"Capítulo 271 — Sentimientos sinceros"),(16107,"Capítulo 272 — La eterna batalla"),(16666,"Capítulo 273 — Las victimas de la guerra santa"),(17053,"Capítulo 274 — El ángel caído de la desesperación, Mael")]
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
