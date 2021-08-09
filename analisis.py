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

from datetime import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
nombre_del_documento = "/energydata_complete.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento


if __name__ == "__main__":
	#datos=np.genfromtxt(input_dir, delimiter=';', dtype='float',skip_header=1, usecols = range(1,21))
	datos=np.genfromtxt(input_dir, delimiter=';', dtype='str',skip_header=1, usecols = (6))
	#datos=np.genfromtxt(input_dir, delimiter=';', dtype=[(0,str),('6',float)],skip_header=1, usecols = (0,6))
	
	print(datos[100])