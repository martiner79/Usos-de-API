import requests
from pprint import pprint
from datetime import datetime

#Latitud de la Provincia de Mendoza
lat = -32.89084

#Longitud de la Ptovincia de Mendoza
lon = -68.82717

api_key = "92690bcd0447a1c81cf8ef96360e6987"

#A nuestra URL le agregamos units=metrics para valores en grados Celcius (°C) y lang=es para la traducción a Español
api_call = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"

r = requests.get(api_call).json()
print("\nPronóstico del Tiempo en 5 dias:\n")

for dato in r['list']:
    print()
    pprint(f"Hora y fecha: {datetime.fromtimestamp(dato['dt'])}")
    pprint(f"Temperatura: {dato['main']['temp']}")
    pprint(f"Descripción: {dato['weather'][0]['description']}")
    

