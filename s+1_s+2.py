#%matplotlib inline  # for IPython notebook

import numpy as np
import matplotlib.pyplot as plt

w=np.linspace(-10, 10, 100)   #representing real frequency from -10 to 10
a = np.ones((1,100),float)

nom = 1j*w+a[0]
denom =1j*w+2*a[0]
h=nom/denom

ang = np.angle(h, deg=True)

#for debug
#print(w)
#print(nom)
#print(denom)
#print(h)
#print(ang)

plt.figure()
plt.plot(w,ang)
