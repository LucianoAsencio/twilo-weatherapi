# Este script extrae los datos del clima de Mar del Plata mediante WeatherAPI y 
# los envía por whatsapp gracias a la librería de Twilo

import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests

# Esta línea carga el archivo '.env' como variables de entorno dentro del mismo directorio.

load_dotenv()

# Obtenemos tanto las credenciales de Twilo como los numeros de entrada y salida mediante
# variables de entorno que seteamos en el archivo ".env"
# Y también la clave de acceso a la API de WeatherAPI

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
whatsapp_remitente = os.getenv("FROM_WHATSAPP_NUMBER")
whatsapp_destino = os.getenv("TO_WHATSAPP_NUMBER")
api_key = os.getenv("WEATHER_API_KEY")


# Se guarda una request a Weather API en Mar del Plata
r = requests.get(url=f'https://api.weatherapi.com/v1/current.json?key={api_key}&q=Mar%20del%20Plata&aqi=no', headers={'Accept': 'application/json'})


# Se lee la request y se guarda en un diccionario
diccionario = r.json()

# Se localiza la información redundante dentro del diccionario
info = diccionario['current']['condition']
condicion = info['text']
icon_url = info['icon']
temperatura = diccionario['current']['temp_c']
humedad = diccionario['current']['humidity']

# Armamos el mensaje a enviar
mensaje = f'El día está {condicion} \nla temperatura es de {temperatura}º\ny la humedad es de {humedad}%'

# Se instancia el objeto Client con la SID de la cuenta y el token de acceso
client = Client(account_sid, auth_token)

# Se crea y envía el mensaje por whatsapp
message = client.messages \
     .create(
        body=mensaje,
        media_url=f'https:{icon_url}',
        from_=whatsapp_remitente,
        to=whatsapp_destino
     )

# Imprimimos por consola el SID del mensaje
# print(message.sid)