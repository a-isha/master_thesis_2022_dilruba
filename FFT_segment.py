# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:44:07 2022

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:22:19 2022

@author: User
"""

import matplotlib.pyplot as plt
import load_from_df
import spectra_signals as spc
#import railData2 as RD

def showFFT(spectrogram_x,spectrogram_y,spectrogram_z, time_slice): 
    
    z_slice = spectrogram_z[284:358,:] ##make sure you understand what part of signal/
    #print(z_slice)
                                    ## what legnth the FFT
    y_slice = spectrogram_y[:10,:]
    x_slice = spectrogram_x[:10,:]
    
    fig = plt.figure(figsize=(8, 6))
    
    plt.subplot(311)
    plt.plot(z_slice[time_slice,:], label = "Z Axis")
    plt.legend(loc=0)
    #print(z_slice[1,:])
    
    plt.title('FFT')
    plt.ylabel('Amplitude')
    #plt.xlabel('Frequency (Hz)')
    
    plt.subplot(312)
    plt.plot(y_slice[time_slice,:], label = "Y Axis")
    plt.legend(loc=0)
    #print(y_slice[1,:])
    
    plt.ylabel('Amplitude')
    #plt.xlabel('Frequency (Hz)')
    
    plt.subplot(313)
    plt.plot(x_slice[time_slice,:], label = "X axis")
    plt.legend(loc=0)
    #print(x_slice[1,:])
    
    plt.ylabel('Amplitude')
    plt.xlabel('Frequency (Hz)')
    
    return z_slice


