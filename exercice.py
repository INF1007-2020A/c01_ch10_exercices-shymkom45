#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([[np.sqrt(i[0]**2 + i[1]**2), np.arctan2(i[1], i[0])] for i in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    closest_index = values.size - 1
    for i in range(values.size - 1):
        if abs(number - values[i]) < abs(number - values[closest_index]):
            closest_index = i
    return closest_index


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([[1, 2], [-2, 1], [1, 1], [1, -2], [-2, -1]])))
    print(find_closest_index(np.array([1, 2, 3, 4, 5, 6, 7]), 6.4))