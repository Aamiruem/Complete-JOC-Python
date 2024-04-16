# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:34:21 2024

@author: aamir
"""

#Crowd Computing
from statistics import mean
from scipy import stats
import statistics
import matplotlib.pyplot as plt
Estimates=[17, 6, 12, 3, 15, 8, 10, 11, 19, 14, 7, 9, 4, 1, 2, 20, 5, 18, 13, 16]
Estimates.sort()
m = stats.trim_mean(Estimates, 0.1)
print(m)
tv=int(.1*len(Estimates))
Estimates=Estimates[tv:len(Estimates)-tv]
print (mean(Estimates))

y=[5]*len(Estimates)
plt.plot(Estimates,y,'r--')
plt.plot(statistics.mean(Estimates),5,'bs')
plt.plot(statistics.median(Estimates),5,'y^')
plt.plot(10,5,'go')