#!/usr/bin/env python
from __future__ import division
from math import *
import matplotlib.pyplot as plt
import numpy as np
from varying_freq_data import *

"""
Plots the resonances
Last updated: November 9
"""

__author__ = "Eric Yeung"

plt.plot(frequency26, pickup26)
plt.errorbar(frequency26, pickup26, ferror26, perror26, fmt='b+', color = 'r')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
#plt.title('For B = 8436.65 G')

plt.annotate('N = 1', xy=(321, 188.92 + 40), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))
plt.annotate('N = 3', xy=(2730, 326.2 + 40), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))

plt.show()

plt.plot(frequency16, pickup16)
plt.errorbar(frequency16, pickup16, ferror16, perror16, fmt = 'b+', color = 'r')

print np.argmax(pickup16), frequency16[np.argmax(pickup16)] # Outlier?

plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
#plt.title('For B = 5191.79 G')

plt.annotate('N = 1', xy=(203 + 130, 88.52 + 30), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))
plt.annotate('N = 3', xy=(1800, 195.76 + 30), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))

plt.show()

plt.plot(frequency10, pickup10)
plt.errorbar(frequency10, pickup10, ferror10, perror10, fmt = 'b+', color = 'r')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
#plt.title('For B = 3244.87 G')

plt.annotate('N = 1', xy=(136, 43.12 + 15), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))
plt.annotate('N = 3', xy=(1100 - 20, 115.75 + 20), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))

plt.show()


####################################################################################


plt.plot(frequency26, pickup26, color = 'g', label = 'B = 8436.65 G')
plt.errorbar(frequency26, pickup26, ferror26, perror26, fmt='b+', color = 'r')
plt.plot(frequency16, pickup16, color = 'b', label ='B = 5191.79 G')
plt.errorbar(frequency16, pickup16, ferror16, perror16, fmt = 'b+', color = 'black')
plt.plot(frequency10, pickup10, color = 'maroon', label = 'B = 3244.87 G')
plt.errorbar(frequency10, pickup10, ferror10, perror10, fmt = 'b+', color = 'dodgerblue')

plt.xlim([0, 1000])
plt.ylim([0, 250])

freq_ticks = np.arange(0, 1100, 100)
freq_labels = freq_ticks

plt.xlabel('Frequency (Hz)')
plt.xticks(freq_ticks, freq_labels)

plt.ylabel('Amplitude (V)')
#plt.title('n$ = 1$ resonances for Various Magnetic Fields')
plt.legend().draggable()
#plt.savefig('N1_resonance_plot.png', format='png', dpi=1200)

plt.show()

print np.std(frequency26), np.std(frequency16), np.std(frequency10)

