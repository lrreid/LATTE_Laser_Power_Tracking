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

fsize = 14                                  # font size for axis lables, ticks and annotations

data     = np.loadtxt(open("LATTE_Laser_Power_History_big.txt"), skiprows=1)
num2date = [datetime.datetime.strptime(str(int(data[k,0])), '%Y%m%d').date() for k in range(len(data[:,0]))]
dates    = np.array(num2date, dtype='datetime64')

Regen_target = np.array([2.0, 2.0])

Regen_Ene = data[:,2]
PL1_Ene   = np.transpose(np.array([data[:,3]*100]))     # Puse energy in mJ for Powerlite 1
PL2_Ene   = np.transpose(np.array([data[:,4]*100]))     # Puse energy in mJ for Powerlite 2
Full_Ene  = np.transpose(np.array([data[:,5]*100]))     # Puse energy in mJ for Full power

if len(dates) > 30:
    dates     = dates[len(dates)-30:len(dates)]
    Regen_Ene = Regen_Ene[len(dates)-30:len(dates)]
    PL1_Ene   = PL1_Ene[len(dates)-30:len(dates)]
    PL2_Ene   = PL2_Ene[len(dates)-30:len(dates)]
    Full_Ene  = Full_Ene[len(dates)-30:len(dates)]

D_max = np.amax(dates)+1     # Find first data point for min
D_min = np.amin(dates)       # Find most recent data point for max
timespan = np.array([D_min, D_max])

fig, (ax1, ax2)  = plt.subplots(1, 2, figsize=(12,6), sharey=False)
plt.subplot(121)
plt.plot(dates,Regen_Ene,'b-s',label="Regen energy")
plt.plot(timespan, Regen_target, 'r--',label="Target")
plt.xticks(np.arange(min(dates)-5, max(dates)+5, step=5))
plt.yticks(np.arange(0, 4, step=0.5))
plt.axis([D_min, D_max, 1, 3])         # set axes [xmin, xmax, ymin, ymax]
plt.tick_params(labelsize=fsize)
ax1 = plt.gca()                             # Required for axis labels to appear
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
plt.xticks(np.arange(min(dates)-5, max(dates)+5, step=5))
plt.yticks(np.arange(0, 1100, step=200))
plt.axis([D_min, D_max, 0, 800])         # set axes [xmin, xmax, ymin, ymax]
plt.tick_params(labelsize=fsize)
ax2 = plt.gca()                             # Required for axis labels to appear
ax2.set_xlabel('Date', fontsize=fsize)
ax2.set_ylabel('Pulse energy (mJ)', fontsize=fsize)
plt.title('Multipass energy', fontsize=fsize)
plt.grid(True)
fig.autofmt_xdate()   # rotate and align the tick labels so they look better
ax2.xaxis.set_major_formatter(DateFormatter("%d/%m"))
plt.legend(bbox_to_anchor=(0.01, 0.40), loc='upper left', borderaxespad=0.)