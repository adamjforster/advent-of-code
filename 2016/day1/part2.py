#!/usr/bin/python

from sys import exit


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
    locations = [(0, 0)]
    
    for instruction in data.split(','):
        turn, move = split_instruction(instruction)
        direction = MAP[direction][turn]
        
        for dummy in range(move):
            if direction == NORTH:
                y += 1
            elif direction == SOUTH:
                y -= 1
            elif direction == EAST:
                x += 1
            elif direction == WEST:
                x -= 1
                
            new_location = (x, y)
            if new_location in locations:
                print abs(x) + abs(y)
                exit()
            else:
                locations.append(new_location)
