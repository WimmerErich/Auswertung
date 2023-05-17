# Auswertungstool - Basis
# Version: 2.0.0
#
# Status 17.05.2023

# Import

from functions_import import *

## Darstellung Grafik

pic_a = 10
pic_b = 9
pic_a2 = 8
pic_b2 = 5

## Import

name = str('temp_center')
att = str('-rfile.out')
att2 = str('-rfile_2.out')
df = pd.read_csv(name+att,delimiter=' ',  skiprows=2)
df.columns = ['timestep', 'temp_center', 'flowtime', 'def']
print(df)
df2 = pd.read_csv(name+att2,delimiter=' ',  skiprows=2)
df2.columns = ['timestep', 'temp_center', 'flowtime', 'def']
print(df2)

name = str('temperatur_thermolelemente')
att = str('-rfile.out')
att2 = str('-rfile_2.out')
df3 = pd.read_csv(name+att,delimiter=' ',  skiprows=2)
df3.columns = ['timestep', 'temp_TEL1', 'temp_TEL2', 'flowtime', 'def']
print(df3)
df4 = pd.read_csv(name+att2,delimiter=' ',  skiprows=2)
df4.columns = ['timestep', 'temp_TEL1', 'temp_TEL2', 'flowtime', 'def']
print(df4)

figure_1_2(str('fig1'), str('Fig.1 - Temperatur im Zentrum der Probe'), pic_a2, pic_b2,
          str('Zeit [s]'), str('Temperatur[K]'),
          df['flowtime'], df['temp_center'],str('Eintauchen der Probe'),
           df2['flowtime'], df2['temp_center'],str('Eingetauchte der Probe'))

figure_1_2(str('fig2'), str('Fig.2 - Temperatur der Termolemente'), pic_a2, pic_b2,
          str('Zeit [s]'), str('Temperatur[K]'),
          df3['flowtime'], df3['temp_TEL1'],str('Eintauchen der Probe'),
           df4['flowtime'], df4['temp_TEL1'],str('Eingetauchte der Probe'))