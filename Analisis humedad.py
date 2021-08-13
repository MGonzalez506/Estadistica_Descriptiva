#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Curso Proabilidad y Estadística

Tarea #1

Template con lectura de datos en archivo csv
"""
import decimal
import sys
import os
import traceback
import time
import signal
#import fcntl
import string
import re
import csv
import numpy as np
import math
import matplotlib.pyplot as plot
from datetime import datetime, timedelta
from numpy import array
from scipy import stats
import pandas as pd
from pprint import pprint
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



if __name__ == "__main__":
    Datacompleta=pd.read_csv("energydata_complete2.csv")
    Datacompleta2=pd.read_csv("energydata_complete2.csv")

    Data_humedad=pd.read_csv('energydata_complete2.csv',usecols=['RH_2'])
    Data_fecha=pd.unique(Datacompleta['date'])
    """
    print(len(Data_humedad))
    print(Data_humedad)
    print(Data_fecha)
    """

    Cuartil1=Datacompleta['RH_2'].quantile(0.25)
    Media=Datacompleta.loc[:,'RH_2'].quantile(0.50) #Calculo de media
    Cuartil2=Datacompleta['RH_2'].quantile(0.75)
    Rango_minimo=Datacompleta['RH_2'].min()
    Rango_maximo=Datacompleta['RH_2'].max()
    Desviacion_standard=Datacompleta['RH_2'].std()
    Numero_de_datos=Datacompleta['RH_2'].count()
    print("Desviacion estandar: ",Desviacion_standard)
    print("Rango minimo: ",Rango_minimo)
    print("Rango maximo: ",Rango_maximo)
    print("---Cuartiles---")
    print("25%: ",Cuartil1)
    print("50%: ", Media)
    print("75%: ",Cuartil2)
    print("Cantidad de datos: ",Numero_de_datos)

    Data_grafico=Datacompleta.groupby('date')['RH_2'].count()

    #print("Prueba grupo: ",Data_grafico)

    Descripcion=Data_humedad.describe(include='all') ##NO UTILIZAR SOLO PARA VERIFICAR
    print(Descripcion) ##NO UTILIZAR SOLO PARA VERIFICAR

    
    Prueba=[]
    Data_ordenada=Data_humedad
    Data_ordenada.sort_values(by=['RH_2'],inplace=True)
    Prueba=Data_ordenada.value_counts(normalize=True) #.cumsum" relativa
    #print(Prueba)

    Tabla_de_frecuencia=[]
    Datacompleta2["Limites"]= pd.cut(Datacompleta2["RH_2"],bins=141)
    Tabla_de_frecuencia=(Datacompleta2
         .groupby("Limites")
         .agg(Frecuencia_absoluta=("RH_2", "count")))
    #Tabla_de_frecuencia["Frecuencia_relativa"]=Prueba[1]
    Tabla_de_frecuencia["Frecuencia_acomulada"]=Tabla_de_frecuencia["Frecuencia_absoluta"].cumsum()
    print(Tabla_de_frecuencia)
    

    plot.hist(x=Data_humedad, bins=141, color='#CCFF03', rwidth=0.85)
    plot.title('- Distribución de datos de las medidas de humedad en la sala -')
    plot.xlabel('Valor de Humedad (%)')
    plot.ylabel('Frecuencia absoluta')
    plot.show()


#print("cantidad de limites: ",len(limites_intervalos))
