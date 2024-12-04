from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#Configuracion del navegador
driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024,720)

#Navegacion a una URL especifica
driver.get('https://courses.academti.com/chatbot/weather-stations/add')
time.sleep(5)

#Crear un diccionario
station_row = {
    'ID':'AEM00041194',
    'Station Name':'DUBAI_INTL',
    'Elev-m':'10.4',
    'Lat':'25.255',
    'Lon':'55.364',
    'Type':'Semiautomatic',
    'Temperature':'1',
    'Atmospheric_Pressure':'0',
    'Humidity':'1',
    'Precipitation':'1',
    'Radiation':'1'
}

#Declaracion de las variables
station_id = station_row['ID']
station_name = station_row['Station Name']
station_elevation = station_row['Elev-m']
station_lat = station_row['Lat']
station_lon = station_row['Lon']
station_type = station_row['Type']
station_temperature = station_row['Temperature']
station_atmospheric = station_row['Atmospheric_Pressure']
station_humidity = station_row['Humidity']
station_precipitation = station_row['Precipitation']
station_radiation = station_row['Radiation']

#Automatizacion del formulario
station_id_element = driver.find_element(By.ID, 'stationId')#Donde colocaremos el id
station_id_element.send_keys(station_id)#mandamos el valor de la llave(AEM00041194) a la pagina
time.sleep(2)

#Name
station_name_element = driver.find_element(By.NAME, 'stationName')
station_name_element.send_keys(station_name)
time.sleep(2)

#Elevation
station_elevation_elemment = driver.find_element(By.CLASS_NAME, 'number')
station_elevation_elemment.send_keys(station_elevation)
time.sleep(2)

#Lat
cordinate_elements = driver.find_elements(By.CLASS_NAME, 'coordinate')
cordinate_elements[0].send_keys(str(station_lat))
time.sleep(2)

#Lon
cordinate_elements[1].send_keys(str(station_lon))
time.sleep(2)
