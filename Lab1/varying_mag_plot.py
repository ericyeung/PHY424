#!/usr/bin/env python
from __future__ import division
from math import *
import matplotlib.pyplot as plt
import numpy as np
from varying_mag_data import *

f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2,3)

ax1.plot(magfield1, v1)
ax1.errorbar(magfield1, v1, xerr = magfield1Error, yerr = v1Error, fmt='b+', color = 'r')
ax1.set_title('(a) 100Hz')

ax2.plot(magfield2, v2)
ax2.errorbar(magfield2, v2, xerr = magfield2Error, yerr = v2Error, fmt='b+', color = 'r')
ax2.set_title('(b) 150Hz')

ax3.plot(magfield3, v3)
ax3.errorbar(magfield3, v3, xerr = magfield3Error, yerr = v3Error, fmt='b+', color = 'r')
ax3.set_title('(c) 200Hz')

ax4.plot(magfield4, v4)
ax4.errorbar(magfield4, v4, xerr = magfield4Error, yerr = v4Error, fmt='b+', color = 'r')
ax4.set_title('(d) 400Hz')

ax5.plot(magfield5, v5)
ax5.errorbar(magfield5, v5, xerr = magfield5Error, yerr = v5Error, fmt='b+', color = 'r')
ax5.set_title('(e) 1000Hz')

ax6.plot(magfield6, v6)
ax6.errorbar(magfield6, v6, xerr = magfield6Error, yerr = v6Error, fmt='b+', color = 'r')
ax6.set_title('(f) 2000Hz')

freq_ticks = [0, 2, 4, 6, 8, 10]
freq_labels = freq_ticks

for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
	ax.set_xlim(0, 10000)

for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
	ax.set_xticklabels(freq_labels)

f.text(0.0, 0.5, 'Amplitude (V)', va='center', rotation='vertical')
ax5.set_xlabel('Magnetic Field (kG)')

plt.tight_layout()
plt.show()
