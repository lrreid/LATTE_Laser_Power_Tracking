# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:18:38 2019

@author: lrreid

Quick script to test the reading and plotting of the history data file

Plotting is now complete and moved to main script
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter

fsize = 12                                  # font size for axis lables, ticks and annotations

data     = np.loadtxt(open("LATTE_Laser_Power_History.txt"), skiprows=1)
num2date = [datetime.datetime.strptime(str(int(data[k,0])), '%Y%m%d').date() for k in range(len(data[:,0]))]
dates    = np.array(num2date, dtype='datetime64')

D_max = np.amax(dates)     # Find first data point for min
D_min = np.amin(dates)     # Find most recent data point for max
Regen_target = np.array([2.0, 2.0])
timespan = np.array([D_min, D_max])

PL1_Ene  = np.transpose(np.array([data[:,2]*100]))     # Puse energy in mJ for Powerlite 1
PL2_Ene  = np.transpose(np.array([data[:,3]*100]))     # Puse energy in mJ for Powerlite 2
Full_Ene = np.transpose(np.array([data[:,4]*100]))     # Puse energy in mJ for Full power


fig, (ax1, ax2)  = plt.subplots(1, 2, figsize=(12,6), sharey=False)
plt.subplot(121)
plt.plot(dates,data[:,1],'b-s',label="Regen energy")
plt.plot(timespan, Regen_target, 'r--',label="Target")
plt.yticks(np.arange(0, 4, step=0.5))
plt.axis([D_min, D_max, 1, 3])         # set axes [xmin, xmax, ymin, ymax]
plt.tick_params(labelsize=fsize)
ax1.set_xlabel('Date', fontsize=fsize)
ax1.set_ylabel('Pulse energy (mJ)', fontsize=fsize)
plt.title('Regen energy', fontsize=fsize)
plt.grid(True)
fig.autofmt_xdate()   # rotate and align the tick labels so they look better
ax1.xaxis.set_major_formatter(DateFormatter("%d/%m"))
plt.legend(bbox_to_anchor=(0.01, 0.20), loc='upper left', borderaxespad=0.)

plt.subplot(122)
plt.plot(dates,PL1_Ene,'b-s', label="Powerlite 1")
plt.plot(dates,PL2_Ene,'g-s', label="Powerlite 2")
plt.plot(dates,Full_Ene,'r-s', label="Full power")
plt.yticks(np.arange(0, 1100, step=200))
plt.axis([D_min, D_max, 0, 1200])         # set axes [xmin, xmax, ymin, ymax]
plt.tick_params(labelsize=fsize)
ax2.set_xlabel('Date', fontsize=fsize)
ax2.set_ylabel('Pulse energy (mJ)', fontsize=fsize)
plt.title('Multipass energy', fontsize=fsize)
plt.grid(True)
fig.autofmt_xdate()   # rotate and align the tick labels so they look better
ax2.xaxis.set_major_formatter(DateFormatter("%d/%m"))
plt.legend(bbox_to_anchor=(0.01, 0.25), loc='upper left', borderaxespad=0.)