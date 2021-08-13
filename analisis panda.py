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



pd.read_csv("surveys.csv")
surveys_df = pd.read_csv("surveys.csv")
print(surveys_df)
print("----------------")
print(surveys_df.head())

type(surveys_df)

print("----------------")

print(surveys_df.dtypes)

surveys_df.columns

surveytest=pd.unique(surveys_df['record_id'])

print("----------------")

print(surveytest)
