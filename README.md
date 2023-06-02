# Usos-de-API
En este repositorio encontrará diferentes usos de API para practicar y entender la metodología de su uso a través del formato json y el lenguaje Python.

Descripción:

1- En el primer archivo “API – dolar” realizamos un proyecto que nos permite saber los valores del dolar oficial y dolar blue (o dolar mercado) gracias a la API https://www.dolarsi.com/api/api.php?type=valoresprincipales . Con la misma también podemos acceder a otros datos, como dolar soja, bitcoin, etc..

2- En el segundo archivo “API – intro” hacemos uso de la API http://api.openweathermap.org para saber los datos del clima. Esto lo realizamos mediante la Latitud, Longitud y nuestra API_key (que nos provee el sitio web cuando nos subscribimos).
En el ejemplo, se usan los datos de la provincia de Mendoza (Argentina)
Sumado a esto, he agregado al enlace lo siguiente:
metric=units → Con esto indicamos que la temperatura se presente en grados celcius (°C)
lang=es → Con esto indicamos que la traducción debe ser en español.

3- En el archivo “API – Proyecto” hemos implementado la API https://wttr.in para realizar la misma función del clima que el archivo anterior, con la diferencia que lo hacemos con otra API, interactuando con otros datos y de manera “personal” con el cliente. Por lo tanto, el usuario podrá elegir la función que desee saber mediante la opción es números. Estos son:
    • Variables del clima
    • Visibilidad
    • Velocidad y Dirección del viento
Por lo tanto, solo debemos colocar el estado o provincia al que pertenecemos en el enlace y los métodos específicos a utilizar.

Si desea saber o estar informado sobre estos temas puede visitar mi sitio web https://lathack.com y encontrar más detalles al respecto.
