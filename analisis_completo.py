#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Proabilidad y Estadística

José Miguel González Arias
Jose Andrés Sandoval Díaz
Alonso Azofeifa Jiménez
"""
#Librerías necesarias para debugging y manejo de excepciones
import sys
import os
import traceback
import time
import signal
import fcntl
import string
import re


"""
Importando pandas para:
- Importar el documento csv
- Obtener las medidas de variabilidad y dispersión de los datos
- Definir los límites para desplegar en pantalla la frecuencia absoluta de los datos
"""
import pandas as pd
from pprint import pprint

#Utilizado para poder construir el diagrama de cajas
import plotnine as p9
from plotnine import *

#Utilizada para crear las diferentes gráficas que muestran el comportamiento 
#de los datos (Histograma y un gráfico lineal)
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#Obtener la figura
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
nombre_del_documento = "/energydata_complete.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento


if __name__ == "__main__":
    
    #Lea el documento CSV ubicado en input_dir, cuyo caracter de separación está dado por ";"
    data = pd.read_csv(input_dir, sep=';')
    #Convierta los datos de la columna 'date', en formato datetime
    data['date'] = pd.to_datetime(data['date'])
    #Ordene todos los datos, respecto a la columna 'date', para ordenar todo respecto a la fecha y hora
    data.sort_values('date', inplace=True)

    #Obtenga los valores promedio de cada día durante todo el estudio
    #Idea de: https://stackoverflow.com/questions/46992158/unable-to-resample-then-plot-a-pandas-data-frame
    data_sampled = data.set_index('date').resample('D').mean().reset_index()
    #La variable x1 será graficada en el eje x y corresponderá a la fecha de los datos tomados
    x1 = data_sampled['date']
    #La variable y1 será graficada en el eje y y corresponderá al valor promedio de un día específico
    y1 = data_sampled['RH_2']

    #Colocando todas las variables necesarias para graficar
    plt.plot_date(x1, y1, linestyle='solid')
    plt.title('Promedio de humedad diario a lo largo del año')
    plt.xlabel('Fecha')
    plt.ylabel('Humedad')
    plt.tight_layout()
    plt.show()

    #Ordenar los datos de menor a mayor de los valores de Humedad.
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
    Data_ordenada=data.sort_values(by=['RH_2'])

    #Obtención de los cuartiles 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#
    Cuartil1=Data_ordenada['RH_2'].quantile(0.25)
    Cuartil2=Data_ordenada.loc[:,'RH_2'].quantile(0.50)
    Cuartil3=Data_ordenada['RH_2'].quantile(0.75)

    #Calculo de media, en este caso la media de calculon en base al cuartil 2 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html?highlight=loc#
    Media=Data_ordenada['RH_2'].mean()
    
    #Calculo de la moda 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html?highlight=mode#
    Moda=Data_ordenada['RH_2'].mode()

    #Obtencion de la mediana 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html
    Mediana=Data_ordenada['RH_2'].median()
    
    #Obtención del rango minimo 
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html
    Rango_minimo=Data_ordenada['RH_2'].min()

    #Obtención del rango maximo
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html
    Rango_maximo=Data_ordenada['RH_2'].max()

    #Obtención de la desviación estandard
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html
    Desviacion_standard=Data_ordenada['RH_2'].std()

    #Obtencion de la desviacioon media
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.mad.html
    Desviacion_media=Data_ordenada['RH_2'].mad()

    #Obtencion de la varianza
    #https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html
    Varianza=Data_ordenada['RH_2'].var(ddof=0)

    #Obtencion del numero de datos que se van a analizar
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html?highlight=count#pandas.DataFrame.count
    Numero_de_datos=Data_ordenada['RH_2'].count()

    #Impresión de los datos antes obtenidos:
    print("\n\n--- Medidas de Variación y Dispersión ---")
    print("Desviación estandar: ",Desviacion_standard)
    print("Desviación media: ",Desviacion_media)
    print("Varianza: ",Varianza)
    print("Rango minimo: ",Rango_minimo) ## REVISAR
    print("Rango maximo: ",Rango_maximo) ##
    print("Media: ", Media)
    print("Moda: ", Moda)
    print("Mediana: ", Mediana)
    
    print("---Cuartiles---")
    print("25%: ",Cuartil1)
    print("50%: ", Cuartil2)
    print("75%: ",Cuartil3)
    print("Cantidad de datos (N): ",Numero_de_datos)

    Data_grafico=data.groupby('date')['RH_2'].count()
    
    Tabla_de_frecuencia=[]
    data["Limites"]= pd.cut(data["RH_2"],bins=141)
    #Obtener una tabla de frecuencia absoluta para comparar luego el histograma
    #El número de clases se calculó como se muestra en la documentación del trabajo
    Tabla_de_frecuencia=(data
         .groupby("Limites")
         .agg(Frecuencia_absoluta=("RH_2", "count")))
    print(Tabla_de_frecuencia)

    graph1=(ggplot(data) +
            geom_boxplot(aes(x=0,y='RH_2'))+
            labs(x="")+
            theme(
                axis_text_x=element_blank(),
                axis_ticks_minor_x=element_blank(),
                axis_ticks_major_x=element_blank()
            ))
    print(graph1)

    plt.hist(x=data['RH_2'], bins=141, color='#CCFF03', rwidth=0.85)
    plt.title('- Distribución de datos de las medidas de humedad en la sala -')
    plt.xlabel('Valor de Humedad (%)')
    plt.ylabel('Frecuencia absoluta')
    plt.grid(True)
    plt.show()