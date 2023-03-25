import matplotlib.pyplot as plt
import numpy as np
import math as math

xpoints = np.linspace(-25,25,100000)
ypoints = xpoints
ypoints2 = xpoints**2

print(xpoints)
print(ypoints)
plt.plot(xpoints, ypoints, ypoints2)
#plt.title("Titulo de prueba")

#plt.grid(color='r', linestyle='-', linewidth=0.5)
plt.show()

#Comentario para probar el commit de Github