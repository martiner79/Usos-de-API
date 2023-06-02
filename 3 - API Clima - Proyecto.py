
import requests
from pprint import pprint

url = "https://wttr.in/buenos%20aires?format=j1&lang=es&metric=units"
r = requests.get(url)
datos = r.json()


def variables_clima():
    temperatura = 'temp_C'
    humedad = 'humidity'
    presion = 'pressure'

    pprint(f"Temperatura: {datos['current_condition'][0][temperatura]}°C")
    pprint(f"Humedad: {datos['current_condition'][0][humedad]} g/m3")
    pprint(f"Presión: {datos['current_condition'][0][presion]} hPa")

def visibilidad():
    visibilidad_km = 'visibility'

    pprint(f"Visibilidad: {datos['current_condition'][0][visibilidad_km]} Km")

def velocidad_dir_viento():
    velocidad_viento = 'windspeedKmph'
    direccion_viento = 'winddir16Point'

    pprint(f"Velocidad del viento: {datos['current_condition'][0][velocidad_viento]} Km/h")
    pprint(f"Dirección del viento: {datos['current_condition'][0][direccion_viento]}")



try:
    r = requests.get(url)
    if r.status_code != 200:
        print("Problema con la conexión al servidor")
except Exception:
        print("ERROR en la página")
else:
    while True:

        #print(f"\nFecha: {date.today()}")
        print()
        pprint(f"Fecha: {datos['weather'][0]['date']}")
        pprint(f"Provincia: {datos['nearest_area'][0]['region'][0]['value']}")
        pprint(f"Localidad: {datos['nearest_area'][0]['areaName'][0]['value']}")
        pprint(f"País: {datos['nearest_area'][0]['country'][0]['value']}")


        print("""
          Bienvenido a los datos del Clima

                ¿Qué desea saber?
        °-----------------------------------°
        1- Variables Climáticas
        2- Visibilidad
        3- Velocidad y Dirección del viento
        4- Salir
        °-----------------------------------°
        """)
    
        try:
            opcion = int(input("Coloque el número correspondiente: "))
        except ValueError:
            print("ERROR: No puede colocar letras.")
        else:
            if opcion == 1:
                print("\nLas Variables del clima son:")
                variables_clima()
            elif opcion == 2:
                print("\nLos datos de visibilidad son:")
                visibilidad()
            elif opcion == 3:
                print("\nLos datos del viento son:")
                velocidad_dir_viento()
            elif opcion == 4:
                print("Vuelva pronto! :)")
                break
            else:
                print("El valor no se encuentra en los datos")






  
    
