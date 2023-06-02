import requests
from pprint import pprint
from datetime import date

url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
r = requests.get(url)

print(f"Fecha: {date.today()}\n")
try:
    if r.status_code == 200:
        datos = r.json()

        pprint("DOLAR OFICIAL:")
        pprint(f"Compra: ${datos[0]['casa']['compra']}")
        pprint(f"Venta: ${datos[0]['casa']['venta']}")

        print()

        pprint("DOLAR BLUE:")
        pprint(f"Compra: ${datos[1]['casa']['compra']}")
        pprint(f"Venta: ${datos[1]['casa']['venta']}")

except ValueError:
    print(f"Error: Problema al Solicitar los datos.")

