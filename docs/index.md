# Bienvenido a la documentación del método RK4

Este módulo considera el método numérico Runge-Kutta de cuarto orden para resolver el problema dinámico de valor inicial:

$$
\frac{dy}{dt} = f(t, y)
$$

el cuál está sujeto a una condición inicial $y(t_0) = y_0$. La función $y = y(t)$ es el estado del sistema en el tiempo $t$.

Específicamente, se toma en consideración el caso en que la función que genera la dinámica temporal para el problema es 

$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$
donde $\mathbf{O}$ es un operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es una operación de conmutación. Notese que la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal, lo cuál se tomará en consideración para su solución.

