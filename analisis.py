#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv
"""
import sys
import os
import traceback
import time
import signal
import fcntl
import string
import re

import csv
import numpy as np
import math
import matplotlib.pyplot as plot

from datetime import datetime, timedelta
from numpy import array
from scipy import stats

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

nombre_del_documento = "/energydata_complete.csv"
#nombre_del_documento = "/data_pag_24_lec_02.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento

timestamp_format = "%d/%m/%Y %H:%M"

if __name__ == "__main__":
	
	str2date = lambda x: datetime.strptime(x.decode('utf-8'), timestamp_format)
	datos=np.genfromtxt(input_dir, delimiter=';', skip_header=1, usecols = (0,6), converters={0: str2date})
	data_humedad = []
	for i in datos:
		data_humedad.append(i[1])
	
	
	
	#https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html
	cantidad_de_datos_n = np.size(data_humedad)
	print("Cantidad de datos: {}".format(cantidad_de_datos_n))

	#https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
	num_clases = math.sqrt(cantidad_de_datos_n)
	#https://parzibyte.me/blog/2019/06/18/python-redondear-numeros/#:~:text=Redondear%20n%C3%BAmeros%20con%20Python,-Vamos%20a%20hacerlo&text=Para%20redondear%20un%20n%C3%BAmero%20basado,lo%20que%20hay%20que%20importarlas.
	num_clases = math.ceil(num_clases)
	print("Número de clases: {}".format(num_clases))

	#Para sacar el máximo de un numpy array: https://numpy.org/doc/stable/reference/generated/numpy.amax.html
	maximo = np.amax(data_humedad)
	print("Maximo: {}".format(maximo))
	minimo = np.amin(data_humedad)
	print("Minimo: {}".format(minimo))
	rango = maximo - minimo
	rango = rango + rango * 0.05
	print("Rango: {}".format(rango))

	intervalo = rango / num_clases
	intervalo = round(intervalo,2)
	print("\n\nIntervalo: {}".format(intervalo))

	step = 0.009
	#step = 0.03

	inicio_de_limite_de_intervalos = minimo - step
	print("Inicio del límite: {}".format(inicio_de_limite_de_intervalos))
	final_de_limite_de_intervalos = maximo + intervalo
	print("Final del límite: {}\n\n".format(final_de_limite_de_intervalos))
	array_de_intervalos = []
	intervalo_temporal = inicio_de_limite_de_intervalos
	while intervalo_temporal<final_de_limite_de_intervalos:
		array_de_intervalos.append(intervalo_temporal)
		intervalo_temporal += intervalo

	print("Cantidad de intervalos: {}\n\n\n".format(np.size(array_de_intervalos)))

	#Función para comparar si dos listas tienen algún dato repetido
	#Esto con el fin de confirmar que no tengamos datos iguales a un límite	
	hay_algun_dato_igual = np.in1d(data_humedad,array_de_intervalos)
	cont = 0
	indice = 0
	for i in hay_algun_dato_igual:
		if i == True:
			cont += 1
			print("Este dato está repetido: {}. Y hay {} datos repetidos".format(i,cont))
			print("El repetido es: {}".format(data_humedad[indice]))
		indice+=1

	res = stats.relfreq(data_humedad, numbins=np.size(array_de_intervalos))
	abso = stats.cumfreq(data_humedad, numbins=np.size(array_de_intervalos))

	print("\n\n\n-------- Tabla de frecuencia de distribución ---------")
	indice = 0
	freq_absoluta = []
	for i in array_de_intervalos[:-1]:
		freq_absoluta.append(i)
	freq_abs_cont = 0
	for i in array_de_intervalos[:-1]:
		os.write(sys.stdout.fileno(), ("\n" + str(array_de_intervalos[indice]) + " < ").encode('utf-8'))
		for ii in data_humedad:
			if array_de_intervalos[indice] < ii and ii < array_de_intervalos[indice+1]:
				#os.write(sys.stdout.fileno(), (str(ii) + ", ").encode('utf-8'))
				freq_abs_cont += 1
				freq_absoluta[indice] = freq_abs_cont
		if freq_abs_cont == 0:
			freq_absoluta[indice] = 0
		freq_abs_cont = 0
		os.write(sys.stdout.fileno(), (" < " + str(array_de_intervalos[indice+1]) + "\n").encode('utf-8'))
		indice += 1

	print("\n\nLa frecuencia absoluta es:")
	print(freq_absoluta)
	print("La cantidad de datos en frecuencia absoluta es: {}".format(np.size(freq_absoluta)))
	print("\nLa frecuencia relativa es:")
	print(res.frequency)

	freq_acumulada = []
	for i in res.frequency:
		freq_acumulada.append(0)
	frecuencia_acumulada_cont = 0
	indice = 0
	for frecuencia in res.frequency:
		frecuencia_acumulada_cont += frecuencia
		freq_acumulada[indice] = frecuencia_acumulada_cont
		indice += 1

	print("\nLa frecuencia acumulada es:")
	print(freq_acumulada)
	print("------------------------\n\n")
	
	plot.hist(x=data_humedad, bins=array_de_intervalos, color='#CCFF03', rwidth=0.85)
	plot.title('- Medidas de humedad en la sala -')
	plot.xlabel('Valor de Humedad (%)')
	plot.ylabel('Frecuencia absoluta')
	#plot.xticks(array_de_intervalos)
	plot.show()
	
	
	


"""
Dato 1 a obtener: Promedio de todas las mediciones
Dato 2 a obtener: Instante en que hubo más humedad -> Año/Mes/Dia Hora/Minuto
Dato 3 a obtener: Instante en que hubo menos humedad -> Año/Mes/Dia Hora/Minuto

La moda de los datos
Lapso de tiempo en que estuvo más constante

Graficar un histograma con los promedios diarios de humedad

Grafica con los promedios diarios de humedad
"""
























