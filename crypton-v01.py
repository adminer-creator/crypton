#/usr/bin/env python
# -*- coding: utf-8 -*-

#
#Tested with python 3 in Debian 10
#
#Probado con python3 con Debian 10
#

import requests
import os
import time
import platform

#In this case we get the data from the api link of bitstamp
#
#En nuestro caso traemos datos desde el link de la api de bitstamp
def get_value_cripto(url='https://www.bitstamp.net/api/v2/ticker/',pair_url='btcusd'):
    #My System Information
    #
    #Mi informacion del sistema
    mysystem = platform.system()
    uname = platform.uname()
    #My Asset - Quantity of each criptocurrency that we own in a tuple- for example this values.
    #This should be modified according to our stock
    #
    #Mi Activo - Cantidades de cada moneda que disponemos ingresados en una tupla- a modo de ejemplo ponemos los valores.
    #Estos deben modificarse de acuerdo a nuestra existencia
    asset_qty = (0.2, 0.7, 200, 300, 50)
    #We define a list with our totals
    #
    #Definimos una lista con los totales
    asset_tot = [0,0,0,0,0]
    myshare = 0
    share = 0
    #We define the tuple with the values - in this example we use Etherum, LitleCoin, Ripple, Stellar and Basic Atenttion Token. Supported currency_pair: btcusd, btceur, btcgbp,
    #btcpax, btcusdt, btcusdc, gbpusd, gbpeur, eurusd, ethusd, etheur, ethbtc, ethgbp, ethpax, ethusdt, ethusdc, xrpusd, xrpeur, xrpbtc, xrpgbp, xrppax, xrpusdt, uniusd, unieur,
    #unibtc, ltcusd, ltceur, ltcbtc, ltcgbp, linkusd, linkeur, linkgbp, linkbtc, linketh, xlmbtc, xlmusd, xlmeur, xlmgbp, bchusd, bcheur, bchbtc, bchgbp, aaveusd, aaveeur, aavebtc,
    #algousd, algoeur, algobtc, snxusd, snxeur, snxbtc, batusd, bateur, batbtc, mkrusd, mkreur, mkrbtc, zrxusd, zrxeur, zrxbtc, yfiusd, yfieur, yfibtc, umausd, umaeur, umabtc, omgusd,
    #omgeur, omggbp, omgbtc, kncusd, knceur, kncbtc, crvusd, crveur, crvbtc, audiousd, audioeur, audiobtc, usdtusd, usdteur, usdcusd, usdceur, usdcusdt, daiusd, paxusd, paxeur, paxgbp, eth2eth, gusdusd
    #For more information: https://www.bitstamp.net/api/
    #Be careful with the max amount of requests over the server, because we can be banned
    #In bitstamp the max requests limits in 10 minutes are 8.000. We can find the info in the web
    #
    #Definimos la tupla con los valores de los pares - a modo de ejemplo definimos Etherum, LitleCoin, Ripple, Stellar y Basic Atenttion Token
    #Para mas información: https://www.bitstamp.net/api/
    #tener cuidado en la cantidad de datos que se transfieren desde los servidores, ya que podemos ser banneados.
    #En bitstamp la cantidad Max de peticiones por 10mins son 8.000. Toda esta informacion la podemos ver en el sitio
    pair_cripto = ('ethusd', 'ltcusd', 'xrpusd', 'xlmusd', 'batusd')
    i = 0
    #print("        Date             | Asset  |   Last   |    Bid   |     Ask")
    #print('+------------------------------------------------------------------------+')
    print(' ')
    print('Crypton v0.1 - System: {}'.format(mysystem), uname.version)
    print(' ')
    print('+--------------------------------+---------+---------+---------+---------+')
    #Title Format
    #
    #Formato de título
    print ( "|{:>15} {:>14}  |{:>7}  |{:>7}  |{:>6}   |{:>7}  |".format('Date','Asset','Last','Bid','Ask','Value'))
    #Loop for five items to look for the tuple data
    #
    #Bucle de 5 para recorrer la tupla con los cinco valores
    while i<5:
        print('+--------------------------------+---------+---------+---------+---------+')
        pair_url=str(url+pair_cripto[i])
        response = requests.get(pair_url)
        if response.status_code == 200:
            #We get the variable with the json content
            #
            #Traemos en nuestra variable el contenido json
            payload = response.json()
            #We assign the all the content from the json data
            #
            #asignamos el dato last/bid/ask/timestamp del contenido json
            results = payload.get('last')
            result1 = payload.get('bid')
            result2 = payload.get('ask')
            result3 = payload.get('timestamp')
            #We transform result3 in date/time format
            #
            #convertimos result3 en formato fecha/hora
            date = time.ctime(int(result3))
            asset_tot[i] = (float(results)*asset_qty[i])
            myshare = myshare + asset_tot[i]
            #We print the lines with the collected data, in some special formats.
            #
            #Imprimimos las líneas con los datos recolectados, en algunos casos con formatos especiales ej. round para redondear con 3 decimales
            print ("|{:<25}{:<7}|{:>8} | {:>7} | {:>7} | {:>7} |".format( date, pair_cripto[i].upper(), results, result1, result2, round(asset_tot[i], 3)))
        i += 1
    print('+--------------------------------+---------+---------+---------+---------+')
    print(' ')
    #Calculate Share percent % with each asset
    #
    #Calculamos el porcentaje de cada activo
    i = 0
    while i<5:
        #We calculate the percent according to our total
        #
        #calculamos en porcentajes de acuerdo a nuestro capital total
        share = (100*asset_tot[i])/myshare
        print ("{:>5} : {:>7} -> {:>5} %".format( pair_cripto[i].upper(), asset_qty[i], str(round(share, 2))))
        i += 1

#Main program, the only it does, is call the get_value_cripto() function
#
#Programa principal que lo único que realiza es llamar a la funcion get_value_cripto()
if __name__ == '__main__':
        #os.system('clear')
        #Run function to do
        get_value_cripto()
