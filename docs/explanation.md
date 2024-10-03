## Explicación del método RK4

El método Runge-Kutta de orden 4 es un método numérico perteneciente a una familia de métodos que reciben el mismo nombre. Estos son útiles para la resolución numérica de ecuaciones diferenciales ordinarias, específicamente del problema del valor inicial. 
El método RK4 viene dado por la siguiente ecuación:

$$
y_{n+1} = y_n + \frac{h}{6} \cdot \left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$

donde $\textit{h}$ corresponde al espaciamiento temporal y las $k_i$ se definen como

$$
k_1 = f(t_n, y_n)
$$

$$
k_2 = f\left(t_n + \frac{h}{2}, y_n + \frac{h \cdot k_1}{2}\right)
$$

$$
k_3 = f\left(t_n + \frac{h}{2}, y_n + \frac{h \cdot k_2}{2}\right)
$$

$$
k_4 = f\left(t_n + h, y_n + h \cdot k_3\right)
$$

Cada $k_{i}$ corresponde a una pendiente, de forma que el resultado final $y_{n+1}$ es determinado por el valor $y_{n}$ más una pendiente estimada.
