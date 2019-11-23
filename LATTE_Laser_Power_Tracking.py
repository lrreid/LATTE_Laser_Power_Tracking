# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:29:35 2019

@author: Lewis Reid

Script to input the power of the LATTE laser on a daily basis
- GUI written to make data input easy
- Values saved to text file
- Plots made to show the laser performance over time

Still to be done:
    - All the plotting
    - Warning for entries containing the same date and how this has to be delt with
    - 
"""


import tkinter as tk
import datetime

# Add an exit button
def close_window():
    window.destroy()
    exit()

# Functions for GUI buttons
def save():
    date       = Date.get() 
    Regen      = float(Regen_Ene.get())
    Powerlite1 = float(PL1_Pow.get())
    Powerlite2 = float(PL2_Pow.get())
    Full_Power = float(Full_Pow.get())
    fp =  open("LATTE_Laser_Power_History.txt","a")            # create text file, 'w' for write, 'a' for append.
    # fp.write("%s\t %s\t %s\t %s\t %s\n" % ("date", "Regen energy (mJ)", "Powerlite 1 (W)", "Powerlite 2 (W)", "Full power (W)"))
    fp.write("%s\t %0.2f\t %0.2f\t %0.2f\t %0.2f\n" % (date, Regen, Powerlite1, Powerlite2, Full_Power))
    fp.close()
    
def plot():
    print("Button doesn't do anything yet")


today = datetime.date.today().__str__()

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