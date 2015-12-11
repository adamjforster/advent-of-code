#!/usr/bin/python

UP = '('
DOWN = ')'


with open('input.txt', 'r') as f:
    data = f.read()
    level = 0
    
    for position, command in enumerate(data):
        if command == UP:
            level += 1
        else:
            level -= 1

        if level == -1:
            print position + 1
            break
