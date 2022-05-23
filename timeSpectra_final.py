# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:16:25 2022

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import load_from_df
import datafiles as data
import spectra_signals as spc

import railData2 as RD

#file number
x = 0

filelist = data.filelist

filename = filelist[x]

path =  "F:/USN/_Thesis/Files from CEMIT/clean_500Hz_63/1560_Breviksbanen_5Hz__" + filename + ".csv"

df = pd.read_csv(path, index_col = None, header = None)

df.reset_index(drop=True, inplace=True)

DF = df
#headers = ["Time","x-axis","y-axis","z-axis","Latitude","Longitude","Velocity","Gyro-x","Gyro-y","Gyro-z"]
DF.columns = ["Time","x-axis","y-axis","z-axis","Latitude","Longitude","Velocity","Gyro-x","Gyro-y","Gyro-z"]
DF = DF.dropna()

# Sampling rate and time vector
fs=500
time_step = 1/fs

time_vec, sig_x, sig_y, sig_z = load_from_df.getSignals(df)

# To see what the data set looks like, we'll use the head() method.

#print(df.head(5))

plt.close("all") 

############################################################
# Spectrogram
############################################################

freqs_x, times, spectrogram_x = spc.spectra_x(sig_x)
freqs_y, times, spectrogram_y = spc.spectra_y(sig_y)
freqs_z, times, spectrogram_z = spc.spectra_z(sig_z)


plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.imshow(spectrogram_x[20:,:], aspect='auto', cmap='jet_r', origin='lower')
#plt.colorbar()
plt.title('Spectrogram (X-Axis)')
plt.ylabel('Frequency band (Hz)')
plt.xlabel('Time window')
#plt.tight_layout(pad=2.0)

#plt.figure(figsize=(10, 6))
plt.subplot(212)
plt.plot(DF.Time, DF.Velocity)
plt.margins(x=0)
plt.ylabel('Velocity')
plt.xlabel('Time')
plt.show()

plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.imshow(spectrogram_y[20:,:], aspect='auto', cmap='jet_r', origin='lower')
#plt.colorbar()
plt.title('Spectrogram (Y-Axis)')
plt.ylabel('Frequency band (Hz)')
plt.xlabel('Time window')
plt.tight_layout()

#plt.figure(figsize=(10, 6))
plt.subplot(212)
plt.plot(DF.Time, DF.Velocity)
plt.margins(x=0)
plt.ylabel('Velocity')
#plt.xlabel('Time')
plt.savefig(filename + "_SpecX", format="png", bbox_inches="tight")
plt.show()


plt.figure(figsize=(10, 6))
plt.subplot(211)
plt.imshow(spectrogram_z[20:,:], aspect='auto', cmap='jet_r', origin='lower')
#plt.pcolormesh(times, freqs_z, spectrogram_z[20:,:])
#plt.colorbar()
plt.title('Spectrogram (Z-Axis)')
plt.ylabel('Frequency band (Hz)')
plt.xlabel('Time window')
plt.tight_layout()
plt.savefig(filename + "_SpecY", format="png", bbox_inches="tight")
plt.show()

#plt.figure(figsize=(10, 6))
plt.subplot(212)
plt.plot(DF.Time, DF.Velocity)
plt.margins(x=0)
plt.ylabel('Velocity')
#plt.xlabel('Time')

plt.savefig(filename + "_SpecZ", format="png", bbox_inches="tight")
plt.show()

############################################################
# Computing and plot of power spectral density (PSD)
############################################################

#The power of the signal per frequency band

Freqs_x, psd1 = signal.welch(sig_x)
Freqs_y, psd2 = signal.welch(sig_y)
Freqs_z, psd3 = signal.welch(sig_z)

plt.figure(figsize=(8, 6))

plt.subplot(311)
plt.plot(Freqs_x[3:], psd1[3:])
plt.title('PSD: power spectral density along X')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()

plt.subplot(312)
plt.plot(Freqs_y[3:], psd2[3:])
plt.title('PSD: power spectral density along Y')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()

plt.subplot(313)
plt.plot(Freqs_z[3:], psd3[3:])
plt.title('PSD: power spectral density along Z')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()

plt.savefig(filename + "_PSD", format="png", bbox_inches="tight")

plt.show()


###########################################################
#Time series data plots
###########################################################

plt.figure(figsize=(10, 8))

plt.subplot(311)
plt.plot(time_vec, sig_x)
plt.ylabel('Amplitude (X-Axis)')
plt.xlabel('Time')
plt.title('Time - Signal')

plt.subplot(312)
plt.plot(time_vec, sig_y)
plt.ylabel('Amplitude (Y-Axis)')
plt.xlabel('Time')
plt.title('Time - Signal')

plt.subplot(313)
plt.plot(time_vec, sig_z)
plt.ylabel('Amplitude (Z-Axis)')
plt.xlabel('Time')
plt.title('Time - Signal')

###########################################################

