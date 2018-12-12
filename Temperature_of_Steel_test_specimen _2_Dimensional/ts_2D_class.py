# -*- coding: utf-8 -*-
import math
import configparser
import numpy as np
from decimal import *

class Loading_input_value :

    def __init__(self):
        pass

    def loading_ini (self) :
        inifile = configparser.ConfigParser()
        inifile.read('./ts_2D_config.ini', 'UTF-8') 
        self.data_save_path = inifile.get('settings', 'data_save_path')
        if inifile.get('settings', 'display_Kelvin') == "True" : self.disp_K = True
        elif inifile.get('settings', 'display_Kelvin') == "False" : self.disp_K = False
        else : print('settings,display_Kelvin Eror')
        self.d_time = inifile.get('settings', 'delta_time')
        self.width_steel = float(inifile.get('Test_Specimens','width_of_steel'))*(10**-3)
        self.heigth_steel = float(inifile.get('Test_Specimens','heigth_of_steel'))* (10**-3)
        self.thickness_FP = float(inifile.get('Test_Specimens','thickness_of_Fireproofing'))*  (10**-3)
        self.total_layer = int( inifile.get('Test_Specimens', 'number_of_layer') )
        self.len_surf = float(inifile.get('Test_Specimens', 'thickness_of_FP_surface'))* (10**-3)
        self.len_Term =  float(inifile.get('Test_Specimens', 'thickness_of_FP_surface'))* (10**-3)
        self.width_TP = self.width_steel + (self.thickness_FP * 2)
        self.heigth_TP = self.heigth_steel + (self.thickness_FP * 2)
        self.len_Tn = (self.thickness_FP - self.len_surf -  self.len_Term)/self.total_layer
        self.test_t = int (inifile.get('settings', 'testing_time'))
        self.temp_DF = float  (inifile.get('default-temperature', 'temperature_of_Furnace'))+273
        self.temp_F = self.temp_DF
        self.temp_FP =  float(inifile.get('default-temperature', 'temperature_of_Fireproofing'))+273
        self.temp_Steel = float(inifile.get('default-temperature', 'temperature_of_Steel'))+273
        self.pf_sh = inifile.get('variable', 'specific_heat_of_Fireproofing')
        self.pf_density = inifile.get('variable', 'density_of_Fireproofing')
        self.steel_density = inifile.get('variable', 'density_of_Steel')

       


class Temperature_calculation:

    def __init__(self,ini_input):

       self.d_time = ini_input.d_time
       self.width_steel = ini_input.width_steel
       self.heigth_steel =ini_input.heigth_steel
       self.thickness_FP = ini_input.thickness_FP 
       self.total_layer = ini_input.total_layer
       self.len_surf = ini_input.len_surf
       self.len_Term =  ini_input.len_Term
       self.width_TP = ini_input.width_TP
       self.heigth_TP = ini_input.heigth_TP
       self.len_Tn = ini_input.len_Tn
       self.test_t = ini_input.test_t
       self.temp_DF = ini_input.temp_DF
       self.temp_F = ini_input.temp_F
       self.temp_FP = ini_input.temp_FP
       self.temp_Steel = ini_input.temp_Steel
       self.pf_sh = ini_input.pf_sh
       self.pf_density = ini_input.pf_density
       self.steel_density = ini_input.steel_density

       
     
    def pf_ther_conductivity(self,temp):
        conductivity_pf = 0
        if temp < 400 : conductivity_pf =  0.09 
        elif temp >= 400 and temp < 800 : conductivity_pf = ((0.11/400) * temp) - 0.02 
        elif temp >= 800 : conductivity_pf = ((0.09 / 200) * temp) -0.16   
        else : print('pf conductivity error')    
        return conductivity_pf

    def temperature_furnace(self,times):
        temp_F =345* math.log10(8*times+1)+self.temp_DF
        return temp_F

    def cal_tempMax(self):
        temp_max = self.temperature_furnace(self.test_t)
        self.tempMAX = (temp_max // 100 )*100 + 100
        return self.tempMAX
      

class Fp_Temperature_calculation(Temperature_calculation):

    def fp_temp_cal (self,array_x,array_y,temp_array):
        if temp_array [array_x-1][array_y][0] == 'Air' :pass
        temp_array [array_x][array_y+1][0]
        temp_array [array_x+1][array_y][0]
        temp_array [array_x][array_y-1][0]
        pass

class Steel_Temperature_calculation(Temperature_calculation):

    def steel_temp_cal (self,array_x,array_y,temp_array):
        pass

    

