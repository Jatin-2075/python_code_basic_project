import sys
import matplotlib.pyplot
matplotlib.use('agg')

import matplotlib.pyplot as plt
import numpy as np

ypoints = ([3, 4, 6, 0])

plt.plot(ypoints, 'o:r', ms = 39, linestyle = 'dotted', linewidth = '10')#r is red
plt.show
plt.savefig(sys.stdout.buffer)

#plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# to change marker facr cover
#plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# more line style like  dashed dotted 
'''
short forms are 
ls line style
for dotted :
for dashed --
for color use c
'''