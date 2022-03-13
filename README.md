# Crypton - ES

Crypton es un pequeño programa hecho con Python para poder visualizar Cripto Assets con amplia información gracias al uso de APIS.

Para el uso de este script se necesita tener instalado python3 y las librerias colorama y requests.

En linux esto se puede instalar de la siguiente manera:
`sudo apt install python3 python3-colorama`
`pip install requests`

Para guardar nuestros datos en un archivo csv agreamos csv al ejecutar el archivo seguido de el pair que queramos guardar. Por ejemplo:
    `python3 crypton-02-2022.py csv xrpusd`
En caso de querer almacenar los datos de todos los assets luego del parametro csv agregamos all:
    `python3 crypton-02-2022.py csv all`

Los valores de wallet y de las disponibilidades se cargan desde el archivo data.json

Probado con python 3 con Debian 10/11 y macOS HighSierra

# Crypton - EN

Crypton is a little script made with Python to visualize Cripto Assets with a lot of information thanks to the APIS.

To use this script you need to have python3 and the colorama and requests libraries.
In linux this can be installed like this:
`sudo apt install python3 python3-colorama`
`pip install requests`

To save our data in a csv file we have to add csv when run the script followed by the pai that we want to save. For example:
    `python3 crypton-02-2022.py csv xrpusd`
In case that you want to save the data from all the assets after the csv parameter you should add all:
    `python3 crypton-02-2022.py csv all`

Available wallets and cripto values are load from file data.json

Tested with python 3 in Debian 10/11 y macOS HighSierra
