#!/usr/bin/python

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


KEYPAD = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]


def move(position, instruction):
    new_position = position[:]
    
    if instruction == UP:
        new_position[0] = max(0, position[0] - 1)
    elif instruction == DOWN:
        new_position[0] = min(4, position[0] + 1)
    elif instruction == LEFT:
        new_position[1] = max(0, position[1] - 1)
    elif instruction == RIGHT:
        new_position[1] = min(4, position[1] + 1)

    try:
        if KEYPAD[new_position[0]][new_position[1]] is None:
            raise IndexError
    except IndexError:
        return position
    else:
        return new_position


with open('input.txt', 'r') as f:
    position = [2, 0]
    
    for line in f:
        for instruction in line:
            position = move(position, instruction)
        print KEYPAD[position[0]][position[1]],
