from selenium import webdriver
import time
chromedriver = "C:/Users/Diego Campos/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print driver.find_element_by_id("content").text
driver.close()	