# -*- coding: utf-8 -*-
import os
import ntpath
import xlrd
import xlwt
import pprint
from datetime import datetime
from decimal import *
import ts_2D_class
import tkinter
import tkinter.messagebox

excel_sheet = xlwt.Workbook()
sheet0 = excel_sheet.add_sheet('DATA_sheet')
input_value = ts_2D_class.Loading_input_value()
input_value.loading_ini()
ts2D_TC = ts_2D_class.Temperature_calculation(input_value)
ts2D_Fp = ts_2D_class.Fp_Temperature_calculation(input_value)
ts2D_St = ts_2D_class.Steel_Temperature_calculation(input_value)

temp = 20 +273
piece_TS = [0,0,temp,0]*16
piece_TS = [[["none",20+273] for i in range(5)] for j in range(5)]
piece_name = ['Air','PF','Steel']
piece_input_name = ['Air','PF','PF','PF','Steel']
temp_f_new = 0

for array_x in range(5):
    for array_y in range (5) :
        for array_i in range (0,5):
            for array_j in range (array_i,5):
                piece_TS [array_x][array_j][0] = piece_input_name [array_i]
            if array_i == array_x :break

piece_TS_new = piece_TS

piece_TS_new [0][1][1]=700
for i in range(5):print(piece_TS_new [i],'\n')

for row in range(10):
    #print ('======='+str(row)+'=======')
    #time_minutes = (row/per_UT) / 60

    #temp_Tn_newに代入ループ
    temp_f_new =ts2D_TC.temperature_furnace(row)
    for i in range(5): 
        for j in range (5) :
            if piece_TS [i][j][0] == piece_name [0]:piece_TS_new [i][j][1] = temp_f_new
            elif piece_TS [i][j][0] == piece_name [1]:piece_TS_new [i][j][1] = ts2D_Fp.fp_temp_cal(i,j,piece_TS)
            elif piece_TS [i][j][0] == piece_name [2]:piece_TS_new [i][j][1] = ts2D_St.steel_temp_cal(i,j,piece_TS)
            else : print("Eror")

    #各tempを更新
    piece_TS = piece_TS_new 

for i in range(5):print(piece_TS_new [i],'\n')


#保存
print('\n=====実行完了=====')
root = tkinter.Tk()
root.withdraw()
ret = tkinter.messagebox.askyesno('確認', 'データを保存しますか？')
if ret :
    char_detafile_date =datetime.now().strftime("%m%d_%Y_%H%M%S")
    char_detafile_name = 'TS_2D_DATA'+ char_detafile_date + '.xls'
    setting_path = input_value.data_save_path
    char_detafile_path = os.path.join(setting_path,char_detafile_name)
    print(char_detafile_path)
    excel_sheet.save(char_detafile_path)

