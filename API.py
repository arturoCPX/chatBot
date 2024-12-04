#Importacion de las librerias
from openai import OpenAI
import os

#Definicion del cliente
client = OpenAI(#Entra a la definicion del cliente
    api_key = os.environ.get('OPENAI_API_KEY')#Se hace la asignacion a la variable, obtenemos la apikey desde .env
)

#Creamos la respuesta
response = client.chat.completions.create(
    model = "gpt-3.5-turbo-0125",#Modelo del chatGPT
    temperature=0.2,
    messages = [
        #Primer ROL
        {"role":"system", "content":'''
            Eres un profesor de la Universidad Estatal de Sonora, solo responder preguntas relacionadas al contenido:
            1.- Materia Programacion Avanzada, url://www.ues.mx, dia: Lunes a Viernes
            2.- Materia Programacion Para Dispositivos Moviles, url://www.ues.mx, dia: Lunes a Viernes
            3.- Inteligencia Artificial, url://www.ues.mx, dia: Lunes a Viernes'''},
        #Segundo ROL
        {"role":"user","content":"¿Hola, buenas tardes?"},
        {"role":"user","content":"¿Tienen cursos los dias sabado?"},
        {"role":"user","content":"Los dias sabado solamente se atienden actividades extracurriculares"},
        {"role":"user","content":"¿Las actividades extracurriculares tienen costo?"}
    ]
)

#Enviamos a impresion
print(response)