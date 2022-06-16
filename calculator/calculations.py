"""
Ce module donne acces a un certain nombre de fonctions mathematiques simple

Le module contient les fonctions suivantes:

* `add(a, b)` - qui retourne la somme de deux nombres
* `substract(a, b)` - qui retourne la difference entre deux nombres
* `multiply(a, b)` - qui retourne la multiplication de deux nombres
* `divide(a, b)` - qui retourne la somme de deux nombres

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0
"""

from typing import Union

def add(a : Union[float, int], b: Union[float, int]) -> float:
    """
    Calcule une addition de deux nombres

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: Nombre representant le 1er terme de l'addition
        b: Nombre representant le 2eme terme de l'addition

    Returns:
        Un nombre representant la somme de 'a' et 'b'
    """
    return float(a + b)

def substract(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Calcule une soustraction de deux nombres

    Examples:
        >>> substract(4.0, 2.0)
        2.0
        >>> substract(4, 2)
        2.0

    Args:
        a: Nombre representant le 1er terme de la soustraction
        b: Nombre representant le 2eme terme de la soustraction

    Returns:
        Un nombre representant la difference de 'a' et 'b'
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Calcule une multiplication de deux nombres

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: Nombre representant le 1er terme de la multiplication
        b: Nombre representant le 2eme terme de la multiplication

    Returns:
        Un nombre representant la multiplication de 'a' et 'b'
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int] = 1) -> float:
    """
    Calcule une division de deux nombres

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a: Nombre representant le dividant de la division
        b: Nombre representant le diviseur de la division

    Returns:
        Un nombre representant la division de 'a' par 'b'
    """
    if b == 0:
        raise ZeroDivisionError("Impossible division by 0")
    return float(a / b)