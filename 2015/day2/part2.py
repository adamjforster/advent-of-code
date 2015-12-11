#!/usr/bin/python


def volume(dimensions):
    return reduce(lambda a, b: a * b, dimensions)


def perimeter(dimensions):
    return (dimensions[0] + dimensions[1]) * 2


with open('input.txt', 'r') as f:
    total_length = 0
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        dimensions = line.split('x')
        dimensions = [int(d) for d in dimensions]
        dimensions.sort()
        
        total_length += (volume(dimensions) + perimeter(dimensions))
        
    print total_length
