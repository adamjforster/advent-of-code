#!/usr/bin/python

LEFT = 'L'
RIGHT = 'R'


NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'


MAP = {
    NORTH: {
        LEFT: WEST,
        RIGHT: EAST
    },
    EAST: {
            LEFT: NORTH,
            RIGHT: SOUTH
        },
    SOUTH: {
            LEFT: EAST,
            RIGHT: WEST
        },
    WEST: {
            LEFT: SOUTH,
            RIGHT: NORTH
        },
}


def split_instruction(instruction):
    instruction = instruction.strip()
    return instruction[0], int(instruction[1:])


with open('input.txt', 'r') as f:
    data = f.read()

    x = 0
    y = 0
    direction = NORTH
    
    for instruction in data.split(','):
        turn, move = split_instruction(instruction)
        direction = MAP[direction][turn]
        
        if direction == NORTH:
            y += move
        elif direction == SOUTH:
            y -= move
        elif direction == EAST:
            x += move
        elif direction == WEST:
            x -= move
    
    print abs(x) + abs(y)
