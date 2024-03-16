#!/usr/bin/env python3
"""
This module contains a function that returns a list with each
element of the input list repeated a number of times.
"""
from typing import Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    zoomed_in: Tuple[int, ...] = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
