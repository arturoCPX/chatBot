
#Se requiere importar las siguientes librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Importamos modulos adicionales
from openai import OpenAI
import os

#Creacion del cliente
client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY')
)

#Generar una funcion
def call_endpoint(messages):
    chatgpt_messages_list = [
        {"role":"system","content": '''
          Eres un profesor de la Universidad Estatal de Sonora, solo puedes contestar en relacio al contenido:
          mi correo electronico es: arturo.cpx@gmail.com, mi telefono es:6621918819
          Las materias con las que trabajo en el semestre actual son:
          1.- Programacion Avanzada, url: www.ues.mx, dias: Lunes, Miercoles y Viernes
          2.- Inteligencia Artificial, url: www.ues.mx, dias: Martes y Jueves   '''}
    ]

    chatgpt_response = chatgpt_messages_list + messages

    #Modelo para obtener una respuesta
    chatgpt_response = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        temperature = 0.2,
        messages = messages
    )

    assistant_message = chatgpt_response.choices[0].message.content

    return assistant_message


#Colocarems las opciones
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\artur\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

#Asignamos las opciones como argumento
driver = webdriver.Chrome(options=options)

#Establecemos las dimensiones de la ventana
driver.set_window_size(1024,720)
driver.set_window_position(0,0)

#Implementamos
driver.implicitly_wait(3600)
driver.get("https://web.whatsapp.com/")


while(True):
    #EXPRESIONES XPAD
    #//*[@id="pane-side"]/descendant::span[contains(@aria-label,'unread')]
    #//*[@id="main"]/descendant::div[@role='row']
    #//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span
    #//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]

    #Recuperamos nuevos mensajes
    new_message = driver.find_element(By.XPATH, '//*[@id="pane-side"]/descendant::span[contains(@aria-label,\'unread\')]')#Busca un chat con mensjaes no leidos
    new_message.click()#Abre el chat

    #Obtener los mensajes del usuario
    last_message = driver.find_elements(By.XPATH, '//*[@id="main"]/descendant::div[@role=\'row\']')#Busca todos los mensjaes del chat con row
    last_message = last_message[-1]# y selecciona el ultimo mensaje

    #Enviamos a impresion el mensaje seleccionado
    last_message_text = last_message.find_element(By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')#Encuentra el contenido del mensaje
    print(f'user message:{last_message.text}')#Imprime en consola el texto del ultimo mensaje

    #Establecemos la lista
    message_list = []
    message_list.append({'role':'user','content': last_message.text})

    #Notificar al usuario, que se envio el texto
    print('sending message to lenguaje service')

    #Simulacion de la API
    #api_message = "Mensaje de respuesta desde la API"

    api_message = call_endpoint(message_list)



    message_element = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    message_element.send_keys(f'{api_message}{Keys.ENTER}')#Envaimos el mensjae al usuario del utlimo mensaje, con la tecla ENTER, 
    message_element.send_keys(Keys.ESCAPE)


