#!/usr/bin/python
# -*- coding: utf-8 -*-


#DOCUMENTACION
#https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver

from datetime import datetime
from selenium import webdriver
import time



DRIVER = 'C:\chromedriver.exe'

op1 = input("Cuántas capturas de pantalla necesitas?: ")
op2 = input("Cuánto tiempo necesitas que espere para tomar cada captura?: ")
op3 = input("Cuál es el sitio al que le tomaré la captura?: http://")


for i in range(0,int(op1),1):
    driver = webdriver.Chrome(DRIVER)
    driver.maximize_window()
    driver.get('http://%s' % op3)
    time.sleep(int(op2))
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot = driver.save_screenshot('Captura-%s.png' %now)
    driver.quit()
    print("Captura",i+1," completada")

print("Se ha guardado con éxito")