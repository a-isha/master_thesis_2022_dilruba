# -*- coding: utf-8 -*-
"""
Created on Mon May 16 05:50:59 2022

@author: User
"""

filelist = ["20200721T1145",     ## Direct
            "20200722T1126",
            "20200722T1222",
            "20200727T1121",
            "20200803T0917",
            "20200810T0929", #6
            "20200812T0957", #7
            "20200817T0942", #8
            "20200817T1047", #9         #std very diff
            "20200824T1033", #10
            "20200824T1135",
            "20200825T1050",
            "20200907T0943", #13
            "20200909T1245",
            "20200910T0735", #15
            "20200910T1011", #16
            "20200910T1110",
            ] # 18 files

# filelist = ["20200729T0800",   ## Reverse
#             "20200730T0712",
#             "20200730T1026",
#             "20200827T1107",
#             "20200907T0804",
#             "20200907T1225"
#             ]


## Test files ##

filelist_val = ["20200729T1336"
                "20200730T1204", # kind of average, could be used to test nrmal conditions
                "20200817T1047", 
                "20200910T1110",
                "20200910T1214"] ## no band streaks on the z axis

# D x-axis exception: "20200730T1204", "20200817T1047" (overall), "20200910T1110" (overall), 
# "20200729T1336" - has that weird shape

# R 20200730T1026 - exception in z for reverse, 20200827T1107 crazy in z 












# ax1 = fig.add_subplot(1, 2, 1, projection = '3d')
# vsl.plot3Dx(avg_spectra, freqs_x, times, ax1)

# ax2 = fig.add_subplot(1, 2, 2, projection = '3d')
# vsl.plot3Dx(compare_spectra, freqs_x, times, ax2)

# #fig.colorbar(surf, shrink=0.5, aspect=5)

# # ax3 = fig.add_subplot(1, 3, 3, projection = '3d')
# # vsl.plot3Dx(spectrogram_x, freqs_x, times, ax3)









# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=8)

# for i in range(3):
    
#     ax = fig.add_subplot(1, 2, i+1, projection = '3d')
    
#     #ax1 = fig.add_subplot(3, 2, 1, projection = '3d')
    