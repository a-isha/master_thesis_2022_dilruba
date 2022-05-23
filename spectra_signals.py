# -*- coding: utf-8 -*-
"""
Created on Mon May 16 03:59:34 2022

@author: User
"""

from scipy import signal

# sampling rate
fs = 500

# 'nperseg' in samples, multiply with ts to get duration of time window

def spectra_x(sig_x):

    freqs_x, times, spectrogram_x = signal.spectrogram(sig_x, fs, nperseg=610, window='blackman', noverlap=100) 
    
    return freqs_x, times, spectrogram_x



def spectra_y(sig_y):  

    freqs_y, times, spectrogram_y = signal.spectrogram(sig_y, fs, nperseg=610, window='blackman', noverlap=100)

    return freqs_y, times, spectrogram_y



def spectra_z(sig_z):

    freqs_z, times, spectrogram_z = signal.spectrogram(sig_z, fs, nperseg=610, window='blackman', noverlap=100)
    
    return freqs_z, times, spectrogram_z
    
