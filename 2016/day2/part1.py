#!/usr/bin/python

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def move(position, instruction):
    if instruction == UP:
        position[0] = max(0, position[0] - 1)
    elif instruction == DOWN:
        position[0] = min(2, position[0] + 1)
    elif instruction == LEFT:
        position[1] = max(0, position[1] - 1)
    elif instruction == RIGHT:
        position[1] = min(2, position[1] + 1)
    return position


with open('input.txt', 'r') as f:
    position = [1, 1]
    
    for line in f:
        for instruction in line:
            position = move(position, instruction)
        print KEYPAD[position[0]][position[1]]
