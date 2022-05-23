# -*- coding: utf-8 -*-
"""
Created on Mon May  9 04:42:03 2022

@author: User
"""


import numpy as np
import matplotlib.pyplot as plt
import load_from_df 
import datafiles as data

############################################################
# DataFile Names
###########################################################

#file number
x = 10

filelist = data.filelist

df, DF = load_from_df.get_df(filelist[x])
print(filelist[x])


#plt.close("all")
#############################################################
#Plots
############################################################

# fig = plt.figure(figsize=(10, 8))

# plt.subplot(311)
# plt.plot(DF.t, DF.v, 'g-', label = "time ")
# plt.margins(x=0)
# plt.title('V versus T')
# plt.grid()
# plt.ylabel('v(m/s)')
# plt.xlabel('time(s)')

# plt.subplot(312)
# plt.plot(DF.t, (DF.s/1000), 'r-', label = "s-dir over time")
# plt.margins(x=0)
# #plt.title('V versus S')
# plt.grid()
# plt.ylabel('distance')
# plt.xlabel('time (s)')

# plt.subplot(313)
# plt.plot((DF.s/1000), DF.v, 'b-', label = "s-dir (km)")
# plt.margins(x=0)
# #plt.title('V versus S')
# plt.grid()
# plt.xlabel('S(km)')
# plt.ylabel('v(m/s)')
# plt.tight_layout()

# #plt.savefig(filelist[x] + "_S-File.png", format="png", bbox_inches="tight")

# plt.show()

##########################################################
# S-direction and Co-ordinates
########################################################

fig = plt.figure(figsize=(6, 5))
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = DF.lat
xline = (DF.s/1000)
yline = DF.lon
ax.set_xticks(np.arange(190, 250, 1))
#ax.set_yticks(np.arange(9.67, 9.71, .001))
ax.set_ylabel('Longitude')
ax.set_zlabel('Latitude')
ax.set_xlabel('s-dir', color='red')
ax.plot3D(xline, yline, zline,'red')
plt.tight_layout()

#plt.savefig(filelist[x] + "_S_n_Coord.png", format="png", bbox_inches="tight")

plt.show()

#######################################################
import matplotlib.pyplot as plt
import mplcursors

sc = ax.scatter(xline,yline,zline, s = 0.2)
# by default the tooltip is displayed "onclick"
# we can change it by setting hover to True
cursor = mplcursors.cursor(sc, hover=True)
# by default the annotation displays the xy positions
# this is to change it to the countries name
@cursor.connect("add")

def on_add(sel):
    
    sel.annotation.set_text(DF.iloc[sel.index]['s'])
    #sel.annotation.set_text(DF.iloc[sel.index]['lat'])
    
plt.show()

###########################################################
# Map and S-direction
##########################################################
# plt.figure(figsize=(4, 8))

# plt.plot(DF.v, -(DF.s/1000), 'b-', label = "s-dir (km)")
# plt.margins(x=0)
# plt.title('S versus V')
# plt.xlabel('v(m/s)')
# plt.ylabel('S(km)')

#plt.savefig(filelist[x] + "_Map_n_S.png", format="png", bbox_inches="tight")

plt.show()


