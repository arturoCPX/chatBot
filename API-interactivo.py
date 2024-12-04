#Importacion de las librerias
from openai import OpenAI
import os

#Definicion del cliente
client = OpenAI(#Entra a la definicion del cliente
    api_key = os.environ.get('OPENAI_API_KEY')#Se hace la asignacion a la variable, obtenemos la apikey desde .env
)

#Mensajes
messages = [
        #Primer ROL
        {"role":"system", "content":'''
            Eres un profesor de la Universidad Estatal de Sonora, solo responder preguntas relacionadas al contenido:
            1.- Materia Programacion Avanzada, url://www.ues.mx, dia: Lunes a Viernes
            2.- Materia Programacion Para Dispositivos Moviles, url://www.ues.mx, dia: Lunes a Viernes
            3.- Inteligencia Artificial, url://www.ues.mx, dia: Lunes a Viernes'''},
    ]

#Interactividad
user_message = ''

#declaramos un bucle
while(user_message != 'exit'):
    #Se carga el mensaje del usuario en la variable
    print("Redactar el mensaje del usuario: ")
    user_message = input()

    #Manejo del historial y de los mensajes
    if len(messages) >=1 and len(messages) <=4:
        messages.append({'role':'user','content': user_message})

    else:
        #Colocamos un bulce FOR
        for i in range(3, len(messages), 2):
            messages[i-2] = messages[i]
            messages[i-1] = messages[i+1]

        messages[len(messages)-2] = {'role':'user','content': user_message}
        messages.pop
    #Establecemos la respuesta
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-0125",
        temperature = 0.2,
        messages = messages
    )

    assistan_message = response.choices[0].message.content
    print(f"La API responde de la siguiente manera --> {assistan_message} ")

    #Despues de la llamada a la API
    print("Despues de haber llamado a la API, tenemos la siguiente respuesta -->")
    print(messages)


