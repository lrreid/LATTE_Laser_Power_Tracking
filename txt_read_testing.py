# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:18:38 2019

@author: lrreid

Quick script to test the reading and plotting of the history data file

This is not going well
    - can't plot dates
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime

data  = np.loadtxt(open("LATTE_Laser_Power_History.txt"), skiprows=1)
date = [datetime.strptime(str(int(data[k,0])), '%Y%m%d').date() for k in range(len(data[:,0]))]
Dates = dates.datestr2num(date)

D_max = np.around(np.amax(data[:,0]),0)     # round min wavelength to nearest integer
D_min = np.around(np.amin(data[:,0]),0)     # round max wavelength to nearest integer

fsize = 12                                  # font size for axis lables, ticks and annotations

fig, ax = plt.subplots()
plt.plot(Dates,data[:,1],color=[0, 0, 0.7])
# plt.axis([D_min, D_max, 1, 3])         # set axes [xmin, xmax, ymin, ymax]
plt.tick_params(labelsize=fsize)
ax.set_xlabel('Date', fontsize=fsize)
ax.set_ylabel('Pulse energy (mJ)', fontsize=fsize)
plt.grid(True)
plt.show()