#!/usr/bin/env python
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

"""
Plots resistance of our type 2 superconductor vs temperature 
"""

__author__ = "Eric Yeung"

data = np.loadtxt('final_data_withouttime.txt')

thermocouple_voltage = data[:,0]
voltage = data[:,1]

# Imports the thermocouple modulue by David Bailey 
from thermocouple import thermocouple

# There was a linear offset of the form mx + b, where m = 10 and b = 1.5
for i in range(len(thermocouple_voltage)):
	thermocouple_voltage[i] = 10*thermocouple_voltage[i] + 1.5

temperature = np.array(thermocouple('E', thermocouple_voltage, 'mV'))

"""
Assuming the current changes linearly with as many
spaces as the amount of data points for voltage.
Our initial current was 3.640 mA and the final current
was 4.348 mA. 
"""
current = np.linspace(3.640, 4.348, len(voltage))

# Assuming material is ohmic, use ohm's law
resistance = voltage/current 

# We used 20 mA range so our uncertainity is +/- 0.07%, this is absolute uncert:
currentError = 7e-4*current

# Couldn't find error for lockin, use error of signal generator instead
voltageError = 1e-2*voltage

# For resistance, just add the relative uncertainities... and calculate absolute uncerts of R
resistanceError = (7e-4 + 1e-2)*resistance

# Type E Thermocouple error is +/- 1.7 C or +/- 1 % below 0 C, lets use the relative one
tempError  = 1e-2*temperature
#print temperature, tempError, resistance, resistanceError

# Make the ticks more frequent
temp_ticks = [-190, -180, -170, -160, -150, -140, -130, -120, -110, -100] 
temp_labels = temp_ticks

if __name__ == "__main__": 
	plt.plot(temperature, resistance, color = 'teal') 
	"""
	Errorbars would not show up well in this graph since there are so many timestamps/points,
	but the instructor can choose to display it using the following line of code:

	plt.errorbar(temperature, resistance, tempError, resistanceError, fmt = 'b+', color = 'g')
	"""
	plt.xlabel('Temperature ($^{\circ}$C)')
	plt.ylabel('Resistance $(\Omega)$')
	plt.title('$YBa_2Cu_3$ near low temperatures ($T_c \simeq -172.1 ^{\circ}$C)')
	plt.xlim([min(temperature), -100])
	plt.xticks(temp_ticks, temp_labels)
	plt.annotate("$T_c$", xy=(-172, 0.023 + 0.00045), xycoords='data',
          	xytext=(-180, 0.027), textcoords='data', arrowprops=dict(arrowstyle="->",
            connectionstyle="arc"), bbox=dict(boxstyle="circle", fc="w"))

	fig = plt.gcf()
	fig.canvas.set_window_title('Our Superconductor')
	plt.show()

else:
	print "Hello World!"
