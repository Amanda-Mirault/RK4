import numpy as np

def dyn_generator(oper, state):
    """Generador de la dinámica temporal para un estado genérico.

    Examples:
        >>> import numpy as np
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        array([[0.-0.j 0.+1.j], [0.-1.j 0.-0.j]])

    Args:
        oper (np.array): Matriz que representa al operador lineal.
        state (np.array): Matriz que representa el estado actual.

    Returns:
        (np.array): Retorna el cambio del estado respecto al tiempo debido al operador.
    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """Aplicación del método numérico Runge-Kutta de orden 4 para resolver un problema del valor inicial.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.01)
        array([[0.99, 0.01], [0.01, 0.99]])

    Args:
        func (callable): Función presentada en la ecuación diferencial.
        oper (np.array): Matriz que representa al operador lineal.
        state (np.array): Matriz que representa el estado actual.
        h (float): Variable que contiene el espaciamiento temporal.

    Returns:
        (np.array): Retorna el estado después de un paso temporal h.
    """
    k1 = func(oper, state)
    k2 = func(oper, state + (h*k1) / 2)
    k3 = func(oper, state + (h*k2) / 2)
    k4 = func(oper, state + (h*k3))

    return state + h * (k1 + 2*k2 + 2*k3 + k4) * (1 / 6)
