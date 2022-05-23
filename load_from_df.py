# -*- coding: utf-8 -*-
"""
Created on Mon May 16 04:03:42 2022

@author: User
"""

import pandas as pd

def get_df(filenumber):
    
    path =  "F:/USN/_Thesis/Files from CEMIT/clean_500Hz_63/1560_Breviksbanen_5Hz__" + filenumber + ".csv"
    path2 = "F:/USN/_Thesis/Files from CEMIT/clean_500Hz_63_LP/1560_Breviksbanen_5Hz__" + filenumber + ".csv"
    
    df = pd.read_csv(path, index_col = None, header = None)
    
    df.reset_index(drop=True, inplace=True)
    
    df_s = pd.read_csv(path2, index_col = None)
    df_s = df_s.dropna()
    
    return df, df_s
    
def getSignals(df):

    # time_step = 1/fs
    time_vec = df.iloc[:, 0]
    
    # Time-series data (X, Y, Z)
    X = df.iloc[:, 1].to_numpy()
    Y = df.iloc[:, 2].to_numpy()
    Z = df.iloc[:, 3].to_numpy()
    
    # Signal
    sig_x = X
    sig_y = Y
    sig_z = Z
    
    return time_vec, sig_x, sig_y, sig_z
    
    
    
