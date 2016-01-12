#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
EXPERIMENT 3: NEEL LAB
Latest Revision: November 25 2015, 12:30 pm
"""

__author__ = "Eric Yeung"

data = np.loadtxt('FirstGoodData.txt', comments='#')
times = data[:,0]

"""
Parse data collected by labview
"""

peak = (np.argmax(data[:,2])) # Should be around 1.6 mV

increasingdata = data[:peak,:] 
decreasingdata = data[peak:,:]

wheatvoltage1 = increasingdata[:,1]
wheatvoltage1_error = 0.02*wheatvoltage1
thermocouple_voltage1 = increasingdata[:,2]

wheatvoltage2 = decreasingdata[:,1]
wheatvoltage2_error = 0.02*wheatvoltage2
thermocouple_voltage2 = decreasingdata[:,2]

""" 
Convert type T thermocouple voltage into temperature
"""

from thermocouple import thermocouple 

temperature1 = np.array(thermocouple('T', thermocouple_voltage1, 'mV'))
temperature2 = np.array(thermocouple('T', thermocouple_voltage2, 'mV'))

temperature1_error = 0.0075*temperature1
temperature2_error = 0.0075*temperature2

"""
Start the plotting for wheatstone voltage vs temperature
"""

plt.figure(1)
plt.plot(temperature1, wheatvoltage1, color = 'r', label = 'Heating up')
plt.plot(temperature2, wheatvoltage2, color = 'b', label = 'Cooling down')

# Too many datapoints, uncomment to see the errorbars

#plt.errorbar(temperature1, wheatvoltage1, xerr = temperature1_error,
# yerr = wheatvoltage1_error, fmt = 'b+', color = 'black')
#plt.errorbar(temperature2, wheatvoltage2, xerr = temperature2_error,
# yerr = wheatvoltage2_error, fmt = 'b+', color = 'black')

plt.annotate("", xy = (35.6, 0.15), xycoords='data', xytext = (36.2, 0.15), 
        textcoords='data', arrowprops=dict(arrowstyle="<->"))

plt.annotate('$T_N$', xy=((35.6+36.2)/2, 0.05), xycoords="data", 
        va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))

plt.annotate("", xy = (35.4, 0.48), xycoords='data', xytext = (35.9, 0.48), 
        textcoords='data', arrowprops=dict(arrowstyle="<->"))

plt.annotate('$T_N$', xy=((35.4+35.9)/2, 0.58), xycoords="data", 
        va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))

plt.xlabel('Temperature ($^{\circ}$C)')
plt.ylabel('Wheatstone Voltage (mV)')
plt.title('Heating: $T_N \simeq 35.79 ^{\circ}$C, Cooling: $T_N \simeq 35.6 ^{\circ}$C')
fig = plt.gcf()
fig.canvas.set_window_title('Wheatstone Voltage and Temperature')
plt.legend().draggable()

"""
Finding the strain Delta L/L
"""

R0 = 120; R0Error = 6      # Resistance of strain gauge at 23C (Ohms)
F0 = 110; F0Error = 0.165  # Gauge factor at 23C
TCR = 0.0015*R0            # Temperature Coefficient of Resistance (Ohm/C)
TCGF = 0.0015*F0           # Temperature Coefficient of Gauge Factor (1/C)
T0 = 23                    # Our room temperature (C)
l0 = 5                     # Effective length at 0 strain (mm)

# Wheatstone resistances
R1 = 1000.
R2 = 100.
Rv = 1266.
Vbat = 1.52 

V = Vbat*Rv/(R1+Rv)

"""
Finding the depedence of resistance on temperature 
"""

Rt1 = (V - wheatvoltage1/10)*R2/(Vbat - (V - wheatvoltage1/10))
Rt2 = (V - wheatvoltage2/10)*R2/(Vbat - (V - wheatvoltage2/10))

# When it's heating up
GaugeFactor1 = F0 + TCGF*(temperature1 - T0)
Rtotal1 = R0 + TCR*(temperature1 - T0)
DeltaR1 = Rt1 - Rtotal1
strain1 = DeltaR1/(GaugeFactor1*R0)

# When it's cooling down
GaugeFactor2 = F0 + TCGF*(temperature2 - T0)
Rtotal2 = R0 + TCR*(temperature2 - T0)
DeltaR2 = Rt2 - Rtotal2
strain2 = DeltaR2/(GaugeFactor2*R0)

"""
Start the plotting for strain vs temperature
"""

plt.figure(2)
plt.plot(temperature1, strain1, color = 'r', label = 'Heating up')
plt.plot(temperature2, strain2, color = 'b', label = 'Cooling down')

plt.xlabel('Temperature ($^{\circ}$C)')
plt.ylabel('$\Delta \ell /\ell$')
#plt.yscale('log')
plt.title('Strain as a function of temperature')
fig = plt.gcf()
fig.canvas.set_window_title('Strain and Temperature')
plt.legend().draggable()

# Want to find strain in the 2 ranges of T_N

heatingindices = []
for i in range(len(temperature1)):
    if 35.67 <= temperature1[i] <= 36.16:
        heatingindices.append(i)

coolingindices = [] 
for j in range(len(temperature2)):
    if 35.54 <= temperature2[j] <= 35.82:
        coolingindices.append(j)

# Average out the values of strain in the range of T_N

#heatingstrain = np.average(strain1[heatingindices])
heatingstrain = strain1[heatingindices[-1]] - strain1[heatingindices[0]]
#coolingstrain = np.average(strain2[coolingindices])
coolingstrain = strain2[coolingindices[-1]] - strain2[coolingindices[0]]

"""
Finding the coefficient of thermal expansion of Cr from lab manual equation
"""
Alphasi = 2.52e-6 

AlphaCr1 = np.zeros(len(temperature1) - 1)
AlphaCr2 = np.zeros(len(temperature2) - 1)

# Heating
for i in range(len(temperature1) - 1):
    AlphaCr1[i] = Alphasi + (strain1[i+1] - strain1[i])/(temperature1[i+1]
     - temperature1[i]) - TCR/(R0*GaugeFactor1[i])

# Cooling
for i in range(len(temperature2) - 1):
    AlphaCr2[i] = Alphasi + (strain2[i+1] - strain2[i])/(temperature2[i+1]
         - temperature2[i]) - TCR/(R0*GaugeFactor2[i])

"""
Start the plotting for thermal coeff vs temperature
"""

plt.figure(3)
plt.plot(temperature1[:-1], AlphaCr1, color = 'r', label = 'Heating up')
plt.plot(temperature2[:-1], AlphaCr2, color = 'b', label = 'Cooling down')

plt.xlabel('Temperature ($^{\circ}$C)')
plt.ylabel(r'$\alpha_{Cr}$')
plt.title(r'$\alpha_{Cr}$ as a function of temperature')
fig = plt.gcf()
fig.canvas.set_window_title('Coefficient of Thermal Expansion')
plt.legend().draggable()

"""
Calculating the Latent heat
"""

volumechange = 3*strain1
L = (-1/5.1)*(volumechange*309)
 
if __name__ == "__main__":
    print "The change in strain in the range of T_N when heating is %.3e" % heatingstrain
    print "The change in strain in the range of T_N when cooling is %.3e" % coolingstrain
    print "The width of the transition when heating is %s" % (36.16-35.67)
    print "The width of the transition when cooling is %s" % (35.82-35.54)
    print "The latent heat per unit volume is %s" % L[55] # This is around 35.9
    plt.show()
 