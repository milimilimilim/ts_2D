import os
import ntpath
import xlrd
import xlwt
import pprint
from datetime import datetime
from decimal import *
import tkinter
import tkinter.messagebox

temp = 20 +273

p_T = [[["none",0] for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5): p_T [i][j][1]= 5*i+j
list = [[-1,0],[0,1],[1,0],[0,-1]]


for i in range(5):print(p_T [i],'\n')