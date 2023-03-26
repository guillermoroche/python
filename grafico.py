import matplotlib.pyplot as plt
import numpy as np
import math as math

xpoints = np.linspace(-25,25,100000)
ypoints2 = xpoints**2
ypoints3 = xpoints**3

print(xpoints)
plt.plot(xpoints, ypoints2)
plt.plot(xpoints, ypoints3)
plt.title("Titulo de prueba")
axismargin = 1.1
plt.axis([axismargin*min(xpoints),axismargin*max(xpoints),min(ypoints3),axismargin*max(ypoints3)])
plt.xlabel("Variable independiente")
plt.ylabel("Variable dependiente")
plt.grid()
plt.show()

#Comentario para probar el commit de Github
#Segundo comentario para probar un nuevo tag