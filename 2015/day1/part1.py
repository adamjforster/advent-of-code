#!/usr/bin/python

UP = '('
DOWN = ')'


with open('input.txt', 'r') as f:
    data = f.read()
    print data.count(UP) - data.count(DOWN)
