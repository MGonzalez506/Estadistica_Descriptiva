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

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

nombre_del_documento = "/energydata_complete.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento

timestamp_format = "%d/%m/%Y %H:%M"

if __name__ == "__main__":
	
	str2date = lambda x: datetime.strptime(x.decode('utf-8'), timestamp_format)
	datos=np.genfromtxt(input_dir, delimiter=';', skip_header=1, usecols = (0,6), converters={0: str2date})
	data_humedad = []
	for i in datos:
		data_humedad.append(i[1])
	
	
	
	#https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html
	cantidad_de_datos = np.size(data_humedad)
	print("Cantidad de datos: {}".format(cantidad_de_datos))

	#https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
	num_clases = math.sqrt(cantidad_de_datos)
	#https://parzibyte.me/blog/2019/06/18/python-redondear-numeros/#:~:text=Redondear%20n%C3%BAmeros%20con%20Python,-Vamos%20a%20hacerlo&text=Para%20redondear%20un%20n%C3%BAmero%20basado,lo%20que%20hay%20que%20importarlas.
	num_clases = math.ceil(num_clases)
	print("Número de clases: {}".format(num_clases))

	#Para sacar el máximo de un numpy array: https://numpy.org/doc/stable/reference/generated/numpy.amax.html
	maximo = np.amax(data_humedad)
	minimo = np.amin(data_humedad)
	rango = maximo - minimo
	rango = rango + rango * 0.05
	print("Rango: {}".format(rango))

	intervalo = rango / num_clases
	print("Intervalo: {}".format(intervalo))

	#intervalos = range(min(data_humedad), max(data_humedad) + 2)

	intervalos = range(20, 56)



	plot.hist(x=data_humedad, bins=[20,25,30,35,40,45,50,55,60], color='#CCFF03', rwidth=0.85)
	plot.show()
	"""
	edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]
	intervalos = range(min(edades), max(edades) + 2)
	plot.hist(x=edades, bins=intervalos, color='#F2AB6D', rwidth=0.85)
	plot.title('Histograma de edades - matplotlib - codigopiton.com')
	plot.xlabel('Edades')
	plot.ylabel('Frecuencia')
	plot.xticks(intervalos)
	plot.show()
	"""
	


"""
Dato 1 a obtener: Promedio de todas las mediciones
Dato 2 a obtener: Instante en que hubo más humedad -> Año/Mes/Dia Hora/Minuto
Dato 3 a obtener: Instante en que hubo menos humedad -> Año/Mes/Dia Hora/Minuto

La moda de los datos
Lapso de tiempo en que estuvo más constante

Graficar un histograma con los promedios diarios de humedad

Grafica con los promedios diarios de humedad
"""
























