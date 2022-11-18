#IMPORTACIÓN DE LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

#PARÁMETROS DE EVALUACIÓN
w = 4
y, x = np.ogrid[-w:w:100j, -w:w:100j]

#CONSTANTES
K = 6
U = 4

#VELOCIDADES EN CARTESIANAS
u = U - (2*K)*((x**2 - y**2)/(x**2 + y**2)**2)
v = -(2*K)*((2*x*y)/(x**2 + y**2)**2)

#PARÁMETROS PARA EL PILAR DE REFERENCIA
theta = np.linspace( 0 , 2 * np.pi , 150 )
radius = np.sqrt(2*K/U)
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
#CREACIÓN Y CONFIGURACIÓN DE PLOT
figure, axes = plt.subplots( 1 )
axes.set_aspect( 1 )

#PLOT
plt.streamplot(x, y, u, v, density = 1.5, color = 'orange')
axes.plot( a, b )

#CONFIGURACIONES ADICIONALES
plt.title('Campo de velocidades sobre pilar')
plt.xlabel('X')
plt.ylabel('$Y$')
plt.axis([-4,4,-4,4])
plt.grid(True)

#MUESTRA LA FIGURA
plt.show()
