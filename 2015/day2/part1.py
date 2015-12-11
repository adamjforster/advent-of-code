#!/usr/bin/python


def smallest_side(dimensions):
    dimensions.sort()
    return dimensions[0] * dimensions[1]


def surface_area(dimensions):
    return (
        (2 * dimensions[0] * dimensions[1]) +
        (2 * dimensions[1] * dimensions[2]) +
        (2 * dimensions[2] * dimensions[0])
    )


with open('input.txt', 'r') as f:
    total_area = 0
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        dimensions = line.split('x')
        dimensions = [int(d) for d in dimensions]
        dimensions.sort()
        
        total_area += (smallest_side(dimensions) + surface_area(dimensions))

    print total_area
