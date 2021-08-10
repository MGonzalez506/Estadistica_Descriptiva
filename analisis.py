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

from datetime import datetime, timedelta

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

nombre_del_documento = "/energydata_complete.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento

timestamp_format = "%d/%m/%Y %H:%M"

if __name__ == "__main__":
	
	str2date = lambda x: datetime.strptime(x.decode('utf-8'), timestamp_format)
	datos=np.genfromtxt(input_dir, delimiter=';', skip_header=1, usecols = (0,6), converters={0: str2date})
	
	print(datos[0])