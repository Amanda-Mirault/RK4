import numpy as np

def dyn_generator(oper, state):
        """Generador de la dinámica temporal de un sistema de ecuaciones diferenciales.

        La función establece la dinámica de la evolución temporal de un sistema a través de una operación de conmutación entre un operador lineal y el estado inicial, donde al resultado se le adjunta la constante compleja. El valor de retorno no depende explícitamente de la variable temporal, razón por la cuál no forma parte de la función.

    Examples:
        >>> import numpy as np
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        array([[0.-0.j 0.+1.j], [0.-1.j 0.-0.j]])

    Args:
        oper (np.array): Matriz que representa el operador lineal.
        state (np.array): Matriz que representa el estado actual del sistema.

    Returns:
        np.array: Retorna el cambio del estado `state` respecto al tiempo debido al operador `oper`.
    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """Aplicación del método Runge-Kutta de orden 4 para resolver ecuaciones diferenciales ordinarias numéricamente.

        El método RK4 estima la solución de un problema dinámico de valor inicial a un punto temporal `state`. Estima el siguiente estado del sistema debido a la dinámica temporal dada por la función `func`, el operador lineal y el estado actual.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.01)
        array([[0.99, 0.01], [0.01, 0.99]])

    Args:
        func (callable): Función presentada en el sistema de ecuaciones diferenciales.
        oper (np.array): Matriz que representa un operador lineal.
        state (np.array): Matriz que representa el estado actual del sistema.
        h (float): Variable que contiene el paso temporal.

    Returns:
        np.array: Retorna el estado del sistema después de un paso temporal h.
    """
    k_1 = h * func(oper, state)
    k_2 = h * func(oper, state + (k_1)/2)
    k_3 = h * func(oper, state + (k_2)/2)
    k_4 = h * func(oper, state + k_3)
    return state + (k_1 + 2 * k_2 + 2 * k_3 + k_4) * (1/6)
