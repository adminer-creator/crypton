#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
# Import the necesaries libraries
import requests
import os
import time
import platform
import sys
import json
from colorama import init, Fore
from csv import writer

init(autoreset=True)

# Abrimos el archivo json en el cual tenemos nuestros datos
# Open the json file where we have our data
file = open(os.path.join(sys.path[0], 'data.json'), 'r')
data = json.load(file)

# Definimos y limpiamos variables y diccionarios
# Define and set to 0 variables and dictionaries
pair_cripto = []
asset_qty = []
fiatList = []
fiat_wallet = 0
myshare = 0
share = 0
total = 0
asset_tot = [0, 0, 0, 0, 0, 0, 0, 0]
last = [0, 0, 0, 0, 0, 0, 0, 0]
bid = [0, 0, 0, 0, 0, 0, 0, 0]
ask = [0, 0, 0, 0, 0, 0, 0, 0]
hora = [0, 0, 0, 0, 0, 0, 0, 0]

result_BTC = ' '

# Funcion para agregar datos en el archivo .csv
# Function to add data to the .csv file
def AgregarCsv(i):
    j = 0

    if i >= 0:
        with open('crypton-' + pair_cripto[i] + '.csv', 'a', newline='') as csvfile:
            archivoCsv = writer(csvfile, delimiter=',')
            archivoCsv.writerow([time.ctime(int(hora[i])),pair_cripto[i], asset_qty[i], last[i]])
    else:
        while j <8:
            with open('crypton.csv', 'a', newline='') as csvfile:
                archivoCsv = writer(csvfile, delimiter=',')
                archivoCsv.writerow([time.ctime(int(hora[j])),pair_cripto[j], asset_qty[j], last[j]])
            j += 1
        j = 0

# Cargamos los datos obtenidos del archivo json en una lista
# Save the data gained from the json file in a list
def load_data():
    global fiat_wallet

    i = 0
    while i < len(data['crypto']):
        pair_cripto.append(data['crypto'][i]['pair_cripto'])
        asset_qty.append(float(data['crypto'][i]['asset_qty']))

        i += 1

    i = 0
    while i < len(data['fiat']):
        fiatList.append(float(data['fiat'][i]['wallet' + str(i)]))
        fiat_wallet += fiatList[i]
        i += 1

# Funcion para cargar datos de Fear and Gread Index desde la API
# Function to load data from Fear and Gread Index from the API
def get_value_fearindex():
    global result_NameIndex
    global result_FearIndex

    url_FearIndex = 'https://api.alternative.me/fng/?limit=2'

    response_FearIndex = requests.get(url_FearIndex)
    payload_FearIndex = response_FearIndex.json()
    result_NameIndex = payload_FearIndex.get('name')
    result_FearIndex = payload_FearIndex.get('data')

# Funcion para cargar datos en nuestro diccionario desde la API
# Function to load data in our dictionaries from the API
def get_value_cripto():
    global share
    global myshare
    global result_BTC
    global hora
    global fiat_wallet
    global total

    i = 0

    url = 'https://www.bitstamp.net/api/v2/ticker/'

    pair_BTC = url + 'btcusd'
    response_BTC = requests.get(pair_BTC)
    payload_BTC = response_BTC.json()
    result_BTC = payload_BTC.get('last')

    while i < len(data['crypto']):
        pair_url = str(url+pair_cripto[i])
        response = requests.get(pair_url)

        if response.status_code == 200:
            payload = response.json()
            last[i] = float(payload.get('last'))
            bid[i] = float(payload.get('bid'))
            ask[i] = float(payload.get('ask'))

            hora[i] = float(payload.get('timestamp'))

            asset_tot[i] = (float(last[i])*asset_qty[i])
            myshare = myshare + asset_tot[i]

            i += 1
    i = 0
    total = fiat_wallet + myshare

# Funcion para formatear e imprimir los datos recogidos desde la API
# Function to format and print the data from the API
def print_value_cripto():

    i = 0
    global share
    global myshare

    # Determinamos el sistema operativo + datos de version para mostrar en pantalla y lo guardamos en la variable
    # Get the operating system + data from the OS version to show in the screen and save ir in these two variables
    mysystem = platform.system()
    uname = platform.uname()

    # Se imprime sistema operativo + datos de version
    # Print the operating system + data from the OS version
    print('Crypton v0.2 - System: {}'.format(mysystem) + uname.version)
    print('Data from: data.json')
    print ('Path: ' + os.path.join(sys.path[0]))

    # Se imprime una linea en blanco y luego el precio de BTC con su par USD btcusd en color amarillo
    # Print a white line and then the BTC-USD pair in a yellow color
    print('')
    print(Fore.WHITE + '----------------------' + Fore.YELLOW
          + '  BTC / USD -- > ' + result_BTC + ' ' + Fore.WHITE + ' -------------------')

    # Mostrar caripela triste o contento
    # Print a face sad or happy
    print('                         ' + result_NameIndex + '          ')

    if int(result_FearIndex[0]["value"]) < 45:
        caripela = ":("
    elif int(result_FearIndex[0]["value"]) > 55:
        caripela = ":)"
    else:
        caripela = ":|"

    print('                     Now ->',
          result_FearIndex[0]["value"], '%  ', caripela, '  ', result_FearIndex[0]["value_classification"])

    if int(result_FearIndex[1]["value"]) < 45:
        caripela = ":("
    elif int(result_FearIndex[1]["value"]) > 55:
        caripela = ":)"
    else:
        caripela = ":|"

    print('               Yesterday ->',
          result_FearIndex[1]["value"], '%  ', caripela, '  ', result_FearIndex[0]["value_classification"])

    # Se imprime los títulos del encabezado de los datos
    # Print the data titles in the header
    print('+------------------------+---------+----------+----------+---------+')
    print("|{:>8}{:>15} |{:>7}  |{:>8}  |{:>6}    |{:>7}  |".format(
        'Date', 'Asset', 'Last', 'Bid', 'Ask', 'Value'))

    # El siguiente bucle mostramos los datos de los 8 pares seteados mas a arriba
    # In the following loop show the data from the 8 pairs setupped at the begging
    while i < len(data['crypto']):
        date = time.ctime(int(hora[i]))
        print('+------------------------+---------+----------+----------+---------+')
        print("|{:<17}{:<7}|{:>8} | {:>8} | {:>8} | {:>7} | ".format(date[3: 20: 1], pair_cripto[i].upper(
        ), round(last[i], 5), round(bid[i], 5), round(ask[i], 5), format(asset_tot[i], '0.2f')))

        i += 1

    i = 0
    # Imprimimos los totales seteados en color
    # Print the totals in colors
    print('+------------------------+---------+----------+----------+---------+')
    print(Fore.GREEN + ' T. Balance -> ', Fore.GREEN + format(total, '0.3f'), Fore.CYAN + ' T. Fiat ->',
          Fore.CYAN + format(fiat_wallet, '0.2f'), Fore.RED + ' T. Asset -> ', Fore.RED + format(myshare, '0.3f'))
    print(' ')

    # Bucle para mostrar y formatear pares y su correspondiente porcentaje(%) en cartera
    # Loop to show and format pairs and their percent(%) in the wallet
    while i < len(data['crypto']):
        share = (100 * asset_tot[i]) / total
        share2 = (100 * asset_tot[i+1]) / total
        print("       {:>5} :{:>7} -> {:>5} %     {:>5} :{:>7} -> {:>5} %".format(pair_cripto[i].upper(), asset_qty[i], str(
            format(share, '0.2f')), pair_cripto[i+1].upper(), asset_qty[i+1], str(format(share2, '0.2f'))))
        i += 2

    print("       {:>5} :{:>7} -> {:>5} %".format('USDUSD', fiat_wallet, format((100 * fiat_wallet) / total, '0.2f')))
    print(f"\n***To export: add this parameters [csv all] or [csv pair](eg. xrpusd)")
    print("for more info README.md")

    myshare = 0
    share = 0

# Funcion que determina el sistema operativo y limpia la pantalla
# Function that clear the screen depending in the OS
def clear_screen():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':

    # Llamamos a la funcion fear & gread Index
    # We call the fear an gread function
    get_value_fearindex()

    # Llamamos a la funcion load_data
    # We call the load_data function
    load_data()

    # Declaramos estas variables para poder llamar a dos funciones en distito momento
    # Declare these variables to call two functions in a different moment
    m = 0
    n = 0

    while True:
        try:
            # Llamamos a la Funcion para recoger datos de API
            # Call the function to get the data from the API
            get_value_cripto()

            # Contamos 2 hs para poder llamar a la funcion ya que no se actualiza seguido
            # We wait 2 hs to call the function because it doesn't update frequently
            if m == 1800:
                get_value_fearindex()
                m = 0

            # Limpiamos la pantalla
            # Clear the screen
            clear_screen()

            # Llamamos a la Funcion para imprimir datos formateados
            # Calll the function to print all the data
            print_value_cripto()

            # Realizamos esta serie de condiciones if-else para obtener los parametros
            # Realize this series of if-else statements to get the parameters
            if (len(sys.argv) > 2):
                if n == 2 and sys.argv[1] == "csv":
                    if sys.argv[2] in pair_cripto:
                        AgregarCsv(pair_cripto.index(sys.argv[2]))
                    elif sys.argv[2] == "all":
                        AgregarCsv(-1)

                    n = 0

            time.sleep(4)

            m += 1
            n += 1

        # Con el TRY anterior y las dos lineas siguientes, Interrumpimos el programa con CTRL + C
        # With the previous TRY  and the following two lines, Interrupt the script with CTRL + C
        except KeyboardInterrupt:
            clear_screen()
            break
