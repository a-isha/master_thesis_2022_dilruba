# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:22:19 2022

@author: User
"""

import matplotlib.pyplot as plt
import mplcursors

import visuals as vsl
import FFT_segment as ffts
import load_from_df
import spectra_signals as spc
import datafiles as data

############################################################
# DataFile Names
############################################################

#file number
x = 10

filelist = data.filelist

df, DF = load_from_df.get_df(filelist[x])

time_vec, sig_x, sig_y, sig_z = load_from_df.getSignals(df)

# Spectrograms
###############################################################################

freqs_x, times, spectrogram_x = spc.spectra_x(sig_x)
freqs_y, times, spectrogram_y = spc.spectra_y(sig_y)
freqs_z, times, spectrogram_z = spc.spectra_z(sig_z)


#plt.close("all")


# Spectrogram of X-Axis (Lateral) #
##############################################################################    

fig = plt.figure(figsize=(10, 8))

## Subplot 1 - spectrogram ##

plt.subplot(211)
#vsl.showSpectra(spectrogram_x, '(X Axis)')
plt.imshow(spectrogram_x[10:,:], aspect='auto', cmap= 'jet_r', origin='lower')
plt.plot(DF.t, DF.v, 'w-')
plt.plot(DF.t, DF.v)
plt.title('Spectrogram (X-Axis) ' + filelist[x])
plt.ylabel('Frequency band (Hz)')

fig.tight_layout(pad=4.2)

## Subplot 2 - velocity ##

ax1 = fig.add_subplot(212)
ax2 = ax1.twiny()
ax1.plot(DF.t, DF.v, 'g-', label = "velocity along time")
ax2.plot((DF.s/1000), DF.v, 'b-', label = "s-dir (km)")
plt.legend(loc=0)
ax1.margins(x=0)
ax2.margins(x=0)
ax1.grid()
ax1.set_ylabel('velocity (m/s)')
ax1.set_xlabel('time(seconds)', color='g')
#plt.savefig(filelist[x] + "_spec_X.png", format="png", bbox_inches="tight")


    
plt.show()
# Spectrogram of Y-Axis (Longitudinal) ##
##############################################################################

fig = plt.figure(figsize=(10, 8))

## Subplot 1 - spectrogram ##

plt.subplot(211)
plt.imshow(spectrogram_y[10:,:], aspect='auto', cmap= 'jet_r', origin='lower')
plt.plot(DF.t, DF.v, 'w-')
plt.title('Spectrogram (Y-Axis) ' + filelist[x])
plt.ylabel('Frequency band (Hz)')
fig.tight_layout(pad=4.2)

## Subplot 2 - velocity ##

ax1 = fig.add_subplot(212)
ax2 = ax1.twiny()
ax1.plot(DF.t, DF.v, 'g-', label = "velocity along time")
ax2.plot((DF.s/1000), DF.v, 'b-', label = "s-dir (km)")
plt.legend(loc=0)
ax1.margins(x=0)
ax2.margins(x=0)
ax1.grid()
ax1.set_ylabel('velocity (m/s)')
ax1.set_xlabel('time(seconds)', color='g')
#plt.savefig(filelist[x] + "_spec_Y.png", format="png", bbox_inches="tight")


## Spectrogram of Z-Axis (Axial) ##
###############################################################################

fig = plt.figure(figsize=(10, 8))

## Subplot 1 - spectrogram ##

plt.subplot(211)
plt.imshow(spectrogram_z[10:,:], aspect='auto', cmap= 'jet_r', origin='lower')
plt.plot(DF.t, DF.v, 'w-')
plt.title('Spectrogram (Z-Axis) ' + filelist[x])
plt.ylabel('Frequency band (Hz)')

fig.tight_layout(pad=4.2)

## Subplot 2 - velocity ##

ax1 = fig.add_subplot(212)
ax2 = ax1.twiny()
ax1.plot(DF.t, DF.v, 'g-', label = "velocity along time")
ax2.plot((DF.s/1000), DF.v, 'b-', label = "s-dir (km)")

ax2.legend(loc=0)
ax1.margins(x=0)
ax2.margins(x=0)
ax1.grid()
ax1.set_ylabel('velocity (m/s)')
ax1.set_xlabel('time(seconds)', color='g')
#plt.savefig(filelist[x] + "_spec_Z.png", format="png", bbox_inches="tight")
#ax2.set_xlabel('s (km)', color='b')

sc = ax2.scatter((DF.s/1000),DF.v, s = 0.01)
# by default the tooltip is displayed "onclick"
# we can change it by setting hover to True
cursor = mplcursors.cursor(sc, hover=True)
# by default the annotation displays the xy positions
# this is to change it to the countries name
@cursor.connect("add")

def on_add(sel):
    
    sel.annotation.set_text(DF.iloc[sel.index]['s'])
    #sel.annotation.set_text(DF.iloc[sel.index]['lat'])
    
sc = ax1.scatter(DF.t,DF.v, s = 0.01)
# by default the tooltip is displayed "onclick"
# we can change it by setting hover to True
cursor = mplcursors.cursor(sc, hover=True)
# by default the annotation displays the xy positions
# this is to change it to the countries name
@cursor.connect("add")

def on_add2(sel):
    
    sel.annotation.set_text(DF.iloc[sel.index]['t'])
    #sel.annotation.set_text(DF.iloc[sel.index]['lat'])
    
plt.show()

#z_slice = ffts.showFFT(spectrogram_x, spectrogram_y, spectrogram_z, 9)

# Exporting spectras as excel for Unscrambler import ##

vsl.exportSpectra(spectrogram_z, freqs_z, times, filelist[x], 'Z-axis')
