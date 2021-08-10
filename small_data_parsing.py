#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Ejercicio de prueba para parsear un Datetime correctamente

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

import datetime as dt

from datetime import datetime, timedelta

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

nombre_del_documento = "/small_data.csv"

input_dir= str(THIS_FOLDER) + nombre_del_documento

timestamp_format = "%Y-%m-%d %H:%M"

def date_parser(d_bytes):
	t1 = d_bytes.decode('utf-8')
	t2 = datetime.strptime(t1, timestamp_format)
	return t2
	
if __name__ == "__main__":
	
	convertfunc = lambda x: float(x.strip(b"%"))/100
	names = ("i", "n", "p", "j", "d")
	xx = np.genfromtxt(input_dir, delimiter=",", names=names, converters={'j': convertfunc})
	print(xx)

	str2date = lambda x: datetime.strptime(x.decode('utf-8'), timestamp_format)
	d1 = np.genfromtxt(input_dir, delimiter=",", names=names, usecols=(4), converters={'d': str2date})
	print("\n\nEspacio\n\n")


	print(d1[0]+timedelta(hours=1))





