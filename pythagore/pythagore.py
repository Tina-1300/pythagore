"""
Utilities for Pythagorean theorem.
"""

import math

__creator__ = "Creator : Tina"
__github__ = "GitHub : https://github.com/Tina-1300"
__currentversion__ = "1.4.1"


def is_rectangle(hypotenuse, side_a, side_b):
    "hypotenuse = longest side"
    return math.isclose(hypotenuse**2, side_a**2 + side_b**2, rel_tol=1e-9)


def adjacent_side(hypotenuse, other_side):
    """Return the missing side"""
    return math.sqrt(hypotenuse**2 - other_side**2)


def hypotenuse(side_a, side_b):
    """Return hypotenuse"""
    return math.sqrt(side_a**2 + side_b**2)


def current_version():
    "Return the current version of the library"
    return __currentversion__


def creator():
    "Return the name and profile github of the creator"
    return f"{__creator__}\n{__github__}"