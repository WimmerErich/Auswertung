# File in dem die Funktions für den Import gespeichert werden.


import matplotlib.pyplot as plt
from scipy.interpolate import LinearNDInterpolator
from scipy.interpolate import NearestNDInterpolator
import numpy as np
import pandas as pd
import os

# Hex Codes VOEST:  #0082B4     #50AACD     #91C8DC     #C8E1F0     - Blau
#                   #A5A5A5     #C4C4C4     #E3E3E3                 - Grau
#                   #87D25A     #D7E6B4                             - Grün
#                   #E1D22D     #FAF2B1                             - Gelb

def figure_1(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, xlabel2, ylabel2, xdata1, ydata1, xdata2, ydata2):
    fig, (ax1, ax2) = plt.subplots(2, figsize=(pic_x, pic_y))
    ax1.grid()
    ax1.scatter(xdata1, ydata1, color='#50AACD', edgecolor='k', s=12)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed')
    ax2.grid()
    ax2.scatter(xdata2, ydata2, color='#50AACD', edgecolor='k', s=12)
    ax2.set_xlabel(xlabel2)
    ax2.set_ylabel(ylabel2)
    ax2.set_axisbelow(True)
    ax2.yaxis.grid(color='gray', linestyle='dashed')
    ax2.xaxis.grid(color='gray', linestyle='dashed')

    plt.savefig(name_fig + '.png')
    plt.close()

def figure_1t(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, xdata1, ydata1,T_mean):
    fig, (ax1) = plt.subplots(1, figsize=(pic_x, pic_y))
    ax1.grid()
    ax1.scatter(xdata1, ydata1, color='#50AACD', edgecolor='k', s=12)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed')
    ax1.set_ylim([300,900])

    plt.savefig(name_fig + '.png')
    plt.close()

def figure_1_2(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, xdata1, ydata1,label1, xdata2, ydata2,label2):
    fig, (ax1) = plt.subplots(1, figsize=(pic_x, pic_y))
    ax1.grid()
    ax1.plot(xdata1, ydata1, color='#50AACD', linestyle='-.', linewidth=1, marker="o", markersize=6,
             markeredgecolor='k', label=label1)
    ax1.plot(xdata2, ydata2, color='#A5A5A5', linestyle='-.', linewidth=1, marker="o", markersize=6,
             markeredgecolor='k', label=label2)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed')
    ax1.legend(loc='best')

    plt.savefig(name_fig + '.png')
    plt.close()

def figure_1b(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, xlabel2, ylabel2, xdata1, ydata1, xdata2, ydata2,T_mean):
    fig, (ax1, ax2) = plt.subplots(2, figsize=(pic_x, pic_y))
    ax1.grid()
    ax1.scatter(xdata1, ydata1, color='#50AACD', edgecolor='k', s=12)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed')
    ax2.grid()
    ax2.scatter(xdata2, ydata2, color='#50AACD', edgecolor='k', s=12)
    ax2.set_xlabel(xlabel2)
    ax2.set_ylabel(ylabel2)
    ax2.set_axisbelow(True)
    ax2.yaxis.grid(color='gray', linestyle='dashed')
    ax2.xaxis.grid(color='gray', linestyle='dashed')
    ax2.set_ylim([T_mean-25,T_mean+25])

    plt.savefig(name_fig + '.png')
    plt.close()

# Funktion für 3 D Darstellung
def figure_2(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, zlabel1, xdata1, ydata1, zdata1):
    fig = plt.figure(figsize=(pic_x, pic_y))
    ax = fig.add_subplot(projection='3d')

    ax.scatter(xdata1, ydata1, zdata1, color='#50AACD', edgecolor='k', s=50)
    ax.set_title(title)
    ax.set_axisbelow(True)
    ax.set_xlabel(xlabel1)
    ax.set_ylabel(ylabel1)
    ax.set_zlabel(zlabel1)

    plt.savefig(name_fig + '.png')
    plt.close()

def figure_3(name_fig, title, pic_x, pic_y, xlabel1, ylabel1, xdata1, ydata1, zdata1,ind):
    fig, (ax1) = plt.subplots(1, figsize=(pic_x, pic_y))
    if ind==1:
        plt.pcolormesh(xdata1, ydata1, zdata1, shading='auto',cmap=plt.cm.get_cmap('gnuplot'))
    else:
        plt.pcolormesh(xdata1, ydata1, zdata1, shading='auto', cmap=plt.cm.get_cmap('Spectral'))
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_title(title)
    plt.colorbar()
    plt.savefig(name_fig + '.png')
    plt.close()

def figure_4(name_fig, title, pic_x, pic_y, xlabel1, ylabel1,label1,label2, xdata1, ydata1, xdata2, ydata2):
    fig, (ax1) = plt.subplots(1, figsize=(pic_x, pic_y))
    ax1.grid()
    ax1.plot(xdata2, ydata2, color='#A5A5A5', linewidth=3, label=label2)
    ax1.plot(xdata1, ydata1, color='#50AACD',linestyle='-.', linewidth=1,marker="o", markersize=8,  markeredgecolor='k', label=label1)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel1)
    ax1.set_ylabel(ylabel1)
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.xaxis.grid(color='gray', linestyle='dashed')
    ax1.legend(loc='upper right')

    plt.savefig(name_fig + '.png')
    plt.close()

def interpol(x_coor,y_coor,heatflux,n_x,n_y,pic_a2,pic_b2,name,OS):
    x_min = min(x_coor)
    x_max = max(x_coor)
    y_min = min(y_coor)
    y_max = max(y_coor)

    print(x_min, x_max, y_min, y_max)

    x_new = np.linspace(x_min, x_max, n_x)
    y_new = np.linspace(y_min, y_max, n_y)
    x_new, y_new = np.meshgrid(x_new, y_new)  # 2D grid for interpolation

    x = x_coor.to_numpy()
    y = y_coor.to_numpy()
    hf = heatflux.to_numpy()

    interp = NearestNDInterpolator(list(zip(x, y)), hf)
    Z = interp(x_new, y_new)

    figure_3(name + '_figure3_'+str(OS), 'Fig.3 - Nearest-neighbor interpolation', pic_a2, pic_b2,
             # Datenname_figure / Titel / Abmessungen
             str('x-coordinate [m]'), str('y-coordinate [m]'),
             # Bezeichnungen Achsen 1 (x/y)
             x_new, y_new, Z,0)

    interp = LinearNDInterpolator(list(zip(x, y)), hf)
    Z = interp(x_new, y_new)

    figure_3(name + '_figure4_'+str(OS), 'Fig.4 - linear Interpolation', pic_a2, pic_b2,
             # Datenname_figure / Titel / Abmessungen
             str('x-coordinate [m]'), str('y-coordinate [m]'),
             # Bezeichnungen Achsen 1 (x/y)
             x_new, y_new, Z,0)

    return Z,x_new, y_new,x_min,x_max,n_x,y_min,y_max,n_y


def data_export(x_new,y_new,T,name):

    df3=pd.DataFrame(x_new[:,0],columns=['x'])
    df3['y']=y_new[:,0]
    df3['temperature']=T[:,0]


    # alle Zeilen fehlen noch

    n=x_new.shape[1]
    i=1

    print(df3)

    while i<n:
        df3_app = pd.DataFrame(x_new[:, i], columns=['x'])
        df3_app['y'] = y_new[:, i]
        df3_app['temperature'] = T[:, i]

        #df3.append(df3_app,ignore_index=True)
        df3=pd.concat([df3,df3_app])
        i=i+1

    df3.to_csv('Temperatur_' + str(name) + '_export.csv', index=None)

    return df3

def cp_T(T):

    cp=1.25/10000*T*T+0.322*T+485

    return cp