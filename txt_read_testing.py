# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:18:38 2019

@author: lrreid

Quick script to test the reading and plotting of the history data file


"""
import numpy as np


data  = np.loadtxt(open("LATTE_Laser_Power_History.txt"), skiprows=1)
