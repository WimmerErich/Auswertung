# Auswertungstool - Basis
#
#
# Status 05.01.2023

# Import

import statistics
import matplotlib.dates as mdates
from numpy import exp
import math
import numpy
import pandas
from IPython.display import display
import matplotlib.pyplot as plt
from matplotlib import lines
import numpy as np
from datetime import datetime
import pandas as pd
import plotly.figure_factory as ff
from scipy.optimize import curve_fit
import matplotlib.colors

# Figure 1

index=['Zufallspunkte']
validation ={'x':[1,2,3,4,5,6],
             'y':[1,2,3,4,5,6]}

df_val=pd.DataFrame(validation)
print(df_val)
print(df_val['x'])

fig_name = input("Name of figure (e.g. furnace):")

# Hex Codes VOEST:  #0082B4     #50AACD     #91C8DC     #C8E1F0     - Blau
#                   #A5A5A5     #C4C4C4     #E3E3E3                 - Grau
#                   #87D25A     #D7E6B4                             - Grün
#                   #E1D22D     #FAF2B1                             - Gelb

fig, (ax1,ax2) = plt.subplots(2, figsize=(16, 9))
cmap = plt.get_cmap('Blues')
ax1.plot(df_val['x'],df_val['y'], color='#0082B4',linestyle='-.',marker="o", markersize=10,  markeredgecolor='k',label='Daten')
ax1.set_title("Fig.1 - " + str(fig_name))
ax1.legend(loc='upper left')
ax1.grid(True)
ax1.set_xlabel('x-Achse')
ax1.set_ylabel('y-Achse')
ax1.grid()
ax1.text(0.6, 0.1, 'Text ', horizontalalignment='left', verticalalignment='center', transform=ax1.transAxes, fontsize=10,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
ax2.plot(df_val['x'],df_val['y']*2, color=cmap(0.5), label='Daten 2')
ax2.legend(loc='upper left')
ax2.grid(True)
ax2.set_xlabel('x-Achse')
ax2.set_ylabel('y-Achse')
ax2.grid()

plt.savefig(str(fig_name) + '_figure1.png')
