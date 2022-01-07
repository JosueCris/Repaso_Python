import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from rutinas import *

def calr():
    z1 = (x1-nu)/sigma
    z2 = (x2-nu)/sigma
    w = norm(loc = nu ,scale = sigma).cdf(x1)
    w2 = norm(loc = nu ,scale = sigma).cdf(x2)
    return z1,z2,w,w2

nu = cf("valor de nu: ");
sigma = cf("valor de sigma: ");
x1 = cf("valor de x1: ");
x2 = cf("valor de x2: ");

z1, z2, w, w2 = calr()

if x1==0:
    print("porcentaje: ",w2)
elif x1<nu:
    print("porcentaje: ",1-w)
else:
    print("porcentaje: ",(w-w2)* -1)

x = np.arange(z1,z2,0.0001)
x2 = np.arange(-10,10,0.0001)
y = norm.pdf(x,0,1)
y2 = norm.pdf(x2,0,1)
fig, ax = plt.subplots(figsize = (19,16))
plt.style.use("fivethirtyeight")
ax.plot(x2, y2)
ax.fill_between(x, y, 0, color = "g")
ax.fill_between(x2, y2, 0, alpha = 0.1)
ax.set_xlim([-10, 10])
ax.set_xlabel("numero del elemento fuera del promedio")
ax.set_title("curva gaussiana o distr. normal")
plt.savefig("gaus.png")
plt.show()