from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.set_window_position(0,0)#posicion de la ventana
driver.set_window_size(1024,720)#tama;o de la venta

#Navegacion hacia la pagina de whatsapp
driver.get("https://web.whatsapp.com/")
time.sleep(15)#abre whatsapp 15seg

#Navegacion hacia URL
driver.get("https://www.google.com")
print(driver.title)
time.sleep(15)#cambia a google 15seg

#METODO BACK
driver.back()
print(driver.current_url)
time.sleep(5)#regresa a whatsapp 5seg

#METODO FORWARD
driver.forward()#regresa a google
print(driver.current_url)#devuelve en consola, la url, para vericar la navegacion de forma correcta
time.sleep(15)#script que detiene la ejecucion 15 segundos

#METODO REFRESH
driver.refresh()#Recarga la pagina que esta en el momento
print(driver.current_url)#imprime url actual en consola
time.sleep(15)#pausa

