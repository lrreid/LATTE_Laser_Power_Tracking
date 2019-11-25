# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:29:35 2019

@author: Lewis Reid

Script to input the power of the LATTE laser on a daily basis
- GUI written to make data input easy
- Values saved to text file
- Plots made to show the laser performance over time

Still to be done:
    - Warning for entries containing the same date and how this has to be delt with
    - Stop save button after first press
    - General tiding and comments
"""

import tkinter as tk
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

fsize = 12                                  # font size for axis lables, ticks and annotations

# Add an exit button
def close_window():
    window.destroy()
    exit()

# Functions for GUI buttons
def save():
    today      = Date.get()
    date       = today[6:10]+today[3:5]+today[0:2]
    Regen      = float(Regen_Ene.get())
    Powerlite1 = float(PL1_Pow.get())
    Powerlite2 = float(PL2_Pow.get())
    Full_Power = float(Full_Pow.get())
    fp =  open("LATTE_Laser_Power_History.txt","a")            # create text file, 'w' for write, 'a' for append.
    #fp.write("%s\t %s\t %s\t %s\t %s\n" % ("date", "Regen energy (mJ)", "Powerlite 1 (W)", "Powerlite 2 (W)", "Full power (W)"))
    fp.write("%s\t %0.2f\t %0.2f\t %0.2f\t %0.2f\n" % (date, Regen, Powerlite1, Powerlite2, Full_Power))
    fp.close()
    
def plot():
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


today = datetime.date.today().strftime('%d/%m/%Y').__str__()

# Main
window = tk.Tk()      # Root object, creates blank window
window.title("LATTE Laser power monitoring")
window.configure(background="white")

# create label
tk.Label(window, text="LATTE laser power monitoring",bg="white",fg="black",font="none 10 bold") .grid(row=0, column=0, sticky=tk.W)

# create label
tk.Label(window, text="Date:",bg="white",fg="black",font="none 10 bold") .grid(row=1, column=0, sticky=tk.W)

# create a text entry box
Date = tk.Entry(window, width=20, bg="white",textvariable=today)
Date.insert(0, today)
Date.grid(row=1,column=1,sticky=tk.W)

# create label
tk.Label(window, text="Enter Regen energy [mJ]:",bg="white",fg="black",font="none 10 bold") .grid(row=2, column=0, sticky=tk.W)

# create a text entry box
Regen_Ene = tk.Entry(window, width=20, bg="white")
Regen_Ene.grid(row=2,column=1,sticky=tk.W)

window.grid_rowconfigure(3, minsize=20)         # Add white space between regen and multipass entries

# create label
tk.Label(window, text="Exit of multipass amplifier",bg="white",fg="black",font="none 10 bold") .grid(row=4, column=0, sticky=tk.W)
tk.Label(window, text="Powerlite 1 [W]",bg="white",fg="black",font="none 10 bold") .grid(row=5, column=0, sticky=tk.W)

# create a text entry box
PL1_Pow = tk.Entry(window, width=20, bg="white")
PL1_Pow.grid(row=5,column=1,sticky=tk.W)

tk.Label(window, text="Powerlite 2 [W]",bg="white",fg="black",font="none 10 bold") .grid(row=6, column=0, sticky=tk.W)

# create a text entry box
PL2_Pow = tk.Entry(window, width=20, bg="white")
PL2_Pow.grid(row=6,column=1,sticky=tk.W)

tk.Label(window, text="Full power [W]",bg="white",fg="black",font="none 10 bold") .grid(row=7, column=0, sticky=tk.W)

# create a text entry box
Full_Pow = tk.Entry(window, width=20, bg="white")
Full_Pow.grid(row=7,column=1,sticky=tk.W)

window.grid_rowconfigure(8, minsize=20)         # Add white space before buttons

# add a save button
tk.Button(window, text="Save", width=6, command=save) .grid(row=9,column=0, sticky=tk.W)
tk.Button(window, text="Plot", width=6, command=plot) .grid(row=9,column=1, sticky=tk.W)

window.grid_rowconfigure(10, minsize=20)         # Add white space before buttons

tk.Button(window, text="Exit", width=6, command=close_window) .grid(row=11,column=0, sticky=tk.W)

# run the main loop
window.mainloop()