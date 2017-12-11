# -*- coding: utf-8 -*-

from math import sqrt, pow


INPUT = 312051


square_dimension = int(round(sqrt(INPUT)))
max_address = int(pow(square_dimension, 2))

last_row = range(max_address - 1, max_address - square_dimension, -1)
x_index = last_row.index(INPUT)
y_index = square_dimension

center_index = (square_dimension // 2, square_dimension // 2)

distance = abs(x_index - center_index[0]) + abs(y_index - center_index[1])

print distance
