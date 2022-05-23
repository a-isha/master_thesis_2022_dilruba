# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:58:41 2022

@author: User
"""

import pandas as pd
import spectra_signals as spc

###############################################################################

def findMinimumTimeLength(f):
    
    fileList = f
    t_init = 10000000
    min_val = t_init
    
    for i in fileList:
        
        path =  "F:/USN/_Thesis/Files from CEMIT/clean_500Hz_63/1560_Breviksbanen_5Hz__" + i + ".csv"
        df = pd.read_csv(path, index_col = None, header = None)  
        df.reset_index(drop=True, inplace=True)
        
        time_vec = df.iloc[:, 0]
        V = len(time_vec)
        
        if V < min_val:
            min_val = V     
    
    return min_val

 
def calculateStandardDeviation(avg_s, compare_s, std_s):
    
    std_S  = compare_s - avg_s
    std_s = std_S
    
    return std_s


def getTestSpectra(test_file, s, min_length, tx):
# if tx >= 0:
    
    ## Axis settigs ##
    Sig = 'Sig_'+ s
    
    if Sig == 'Sig_X':
        axis = 1
    elif Sig == 'Sig_Y':
        axis = 2
    else: 
        axis = 3
    #################
        
    Path =  "F:/USN/_Thesis/Files from CEMIT/clean_500Hz_63/1560_Breviksbanen_5Hz__" + test_file[tx] + ".csv"
    DF = pd.read_csv(Path, index_col = None, header = None)  
    DF.reset_index(drop=True, inplace=True) 

    Sig = DF.iloc[:min_length, axis].to_numpy()
    
    # Spectra X
    Freqs, Times, t_s = spc.spectra_x(Sig)
    
    return t_s

###############################################################################