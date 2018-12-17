# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from itertools import cycle


with open('input.txt', 'r') as f:
    frequency = 0
    previous = set([frequency])
    
    for value in cycle(f):
        frequency += int(value)
        
        if frequency in previous:
            print(frequency)
            break
            
        previous.add(frequency)
