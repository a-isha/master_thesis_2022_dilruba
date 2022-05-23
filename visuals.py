# -*- coding: utf-8 -*-
"""
Created on Mon May 16 02:16:00 2022

@author: User
"""
import pandas as pd 
import matplotlib.pyplot as plt 


def exportAverageSpectra(a_df, fq, t, axs):
    
    a_df = pd.DataFrame(a_df) #remove the .T here
    a_df = a_df.T
    
    # Add times to dataframe
    a_df['t'] = t.tolist()
    
    # Add frequency as rows
    f = pd.DataFrame(fq)
    f = f.T
    a_df = a_df.append(f, ignore_index = True)
    
    first_column = a_df.pop('t')   # popping last column to add as first
    a_df.insert(0, '',first_column)
    
    a_df.to_excel(axs + '_avg_spectra.xlsx', index_label = False, index = False)

def exportSpectra(s_df, fq, t, file, axs):
    
    s_df = pd.DataFrame(s_df) #remove the .T here
    s_df = s_df.T
    
    # Add times to dataframe
    s_df['t'] = t.tolist()
    
    # Add frequency as rows
    f = pd.DataFrame(fq)
    f = f.T
    s_df = s_df.append(f, ignore_index = True)
    
    first_column = s_df.pop('t')   # popping last column to add as first
    s_df.insert(0, '',first_column)
    
    s_df.to_excel(file + '_' + axs + '_spectra.xlsx', index_label = False, index = False)

def showSpectra(Sxx, cap):
    
    #plt.close("all")
    fig = plt.figure(figsize=(10, 8))
    
    plt.imshow(Sxx[10:,:], aspect='auto', cmap= 'coolwarm', origin='lower')
    plt.title('Spectrogram ' + cap)
    plt.ylabel('Frequency band (Hz)')
    plt.xlabel('Time window')
    plt.colorbar()
        
    return fig 


def plot3D(Sxx, f, t, fig, C):
  
    spec_x = Sxx[10:,:]
    
    # 3d plot
    ax = fig.gca(projection='3d')
    ax.margins(y=0)
    ax.margins(x=0)
    
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Times")
    ax.set_zlabel("Amp")
    ax.set_zlim([-0.03, 0.05])
    
    surf = ax.plot_surface(f[10:, None], t[None, :], (spec_x), cmap=C)
    
    # Add a color bar which maps values to colors.
    #fig.colorbar(surf, ax=ax, shrink=0.3, aspect=6)
    
    plt.show()
    
    
    
def plot3Dx(Sxx, f, t, ax):

    from matplotlib import cm
        
    spec_x = Sxx[10:,:]
    
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    
    ax.margins(y=0)
    ax.margins(x=0)
    
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Times")
    
    ax.set_zlim([0, 0.05])
    
    #ax.zaxis.set_major_locator(LinearLocator(5))
    # A StrMethodFormatter is used automatically
    #ax.zaxis.set_major_formatter('{x:.01f}')

    #surf = ax.contourf3D(t, f, Sxx, cmap=cm.coolwarm)
    surf = ax.plot_surface(f[10:, None], t[None, :], (spec_x), cmap=cm.coolwarm)
        
    return surf




 
