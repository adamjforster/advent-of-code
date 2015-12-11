#!/usr/bin/python

NORTH = '^'
EAST = '>'
SOUTH = 'v'
WEST = '<'


def move(instruction, location):
    if instruction == NORTH:
        location['y'] += 1
    elif instruction == EAST:
        location['x'] += 1
    elif instruction == SOUTH:
        location['y'] -= 1
    elif instruction == WEST:
        location['x'] -= 1
        
        
def deliver_present(coords, location):
    if location['x'] not in coords:
        coords[location['x']] = {}
    
    if location['y'] not in coords[location['x']]:
        coords[location['x']][location['y']] = 1
    else:
        coords[location['x']][location['y']] += 1


with open('input.txt', 'r') as f:
    data = f.read()
    
    location = {'x': 0, 'y': 0}
    coords = {location['x']: {location['y']: 1}}
    
    for instruction in data:
        move(instruction, location)
        deliver_present(coords, location)

    print sum([len(coords[x_coord]) for x_coord in coords.keys()])
