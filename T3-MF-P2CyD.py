#IMPORTACIÓN DE LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

#PARÁMETROS DE EVALUACIÓN
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)
X, Y = np.meshgrid(x,y)

w = 4
y1, x1 = np.ogrid[-w:w:100j, -w:w:100j]

#CONSTANTES
U = 4
K = 6

#VELOCIDADES EN CARTESIANAS
u = U - (2*K)*((x1**2 - y1**2)/(x1**2 + y1**2)**2)
v = -(2*K)*((2*x1*y1)/(x1**2 + y1**2)**2)

#FUNCIÓN POTENCIAL Y CORRIENTE EN CARTESIANAS     
P = (U*X)+((2*K)*X/(X**2 + Y**2))
I = (U*Y)-((2*K)*Y/(X**2 + Y**2))

#CREACIÓN Y CONFIGURACIÓN DE FIGURA
figure, axes = plt.subplots( 1 )
axes.set_aspect( 1 )

#PLOT
plt.streamplot(x1, y1, u, v, density = 1.5, linewidth=0.8, color = 'orange')
cntr1 = axes.contour(X, Y, P, 85, colors = 'black', linestyles='dashed')
cntr2 = axes.contour(X, Y, I, 85, colors = 'green', linestyles='solid')

#CONFIGURACIONES ADICIONALES
h1,_ = cntr1.legend_elements()
h2,_ = cntr2.legend_elements()
axes.legend([h1[0], h2[0]], ['Potencial', 'Corriente'])
plt.title('Líneas de corriente y potencial + Campo de velocidades')
plt.xlabel('X')
plt.ylabel('$Y$')
plt.axis([-4,4,-4,4])
plt.grid(True)

#MUESTRA FIGURA
plt.show()
